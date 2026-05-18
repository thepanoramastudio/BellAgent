import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from linebot.v3 import WebhookParser
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent, UserSource

from app.config import settings
from app.agents import l1_agent
from app.integrations.line_client import reply, get_display_name
from app.integrations.odoo_client import odoo

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

parser = WebhookParser(settings.line_channel_secret)

ESCALATION_TEAM = {
    "Human-L1": "L1 action",
    "L2-Tech":  "L2-Tech action",
    "L2-Dev":   "L2-Dev action",
}


@asynccontextmanager
async def lifespan(app: FastAPI):
    await odoo.authenticate()
    logger.info("Odoo session authenticated")
    yield
    await odoo.close()


app = FastAPI(title="Bell Agent", lifespan=lifespan)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/webhook")
async def webhook(request: Request):
    signature = request.headers.get("X-Line-Signature", "")
    body = await request.body()

    try:
        events = parser.parse(body.decode("utf-8"), signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    for event in events:
        if isinstance(event, MessageEvent) and isinstance(event.message, TextMessageContent):
            await handle_text_message(event)

    return {"status": "ok"}


async def handle_text_message(event: MessageEvent) -> None:
    user_id = event.source.user_id if isinstance(event.source, UserSource) else "unknown"
    message_text = event.message.text
    reply_token = event.reply_token
    channel_name = getattr(event.source, "group_id", None) or "LINE Direct"

    logger.info(f"Message from {user_id}: {message_text[:80]}")

    try:
        # Step 1 — find existing open ticket or create a new one
        ticket_id = odoo.get_active_ticket(user_id)

        if ticket_id:
            await odoo.add_message_to_ticket(ticket_id, message_text)
            logger.info(f"Message appended to existing ticket #{ticket_id}")
        else:
            display_name = await get_display_name(user_id)
            ticket = await odoo.create_ticket(
                line_user_id=user_id,
                line_display_name=display_name,
                channel_name=channel_name,
                message=message_text,
            )
            ticket_id = ticket["id"]
            odoo.set_active_ticket(user_id, ticket_id)
            logger.info(f"New ticket created: #{ticket_id} for {display_name}")

        # Step 2 — run AI Agent (L1)
        result = await l1_agent.run(message=message_text)
        logger.info(f"Agent decision: {result.action} — {result.payload}")

        if result.action == "answer":
            answer = result.payload["answer"]
            await reply(reply_token, answer)
            await odoo.add_message_to_ticket(ticket_id, f"[Bell AI]: {answer}")
            logger.info(f"Ticket #{ticket_id} answered by AI (kept open)")

        else:
            route_to = result.payload["route_to"]
            reason = result.payload["reason"]
            customer_msg = result.payload["customer_message"]
            action_card = ESCALATION_TEAM.get(route_to, "L1 action")

            await reply(reply_token, customer_msg)
            await odoo.add_message_to_ticket(ticket_id, f"[Escalation → {route_to}]: {reason}")
            await odoo.update_ticket(ticket_id, {"x_studio_action_card": action_card})
            logger.info(f"Ticket #{ticket_id} escalated to {route_to}")

    except Exception as e:
        logger.error(f"Error processing message from {user_id}: {e}", exc_info=True)
        await reply(
            reply_token,
            "ขออภัยครับ/ค่ะ เกิดข้อผิดพลาด กรุณาลองใหม่อีกครั้ง",
        )
