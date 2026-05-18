from linebot.v3.messaging import (
    AsyncApiClient,
    AsyncMessagingApi,
    Configuration,
    ReplyMessageRequest,
    TextMessage,
    PushMessageRequest,
)
import httpx
from app.config import settings

_configuration = Configuration(access_token=settings.line_channel_access_token)


async def reply(reply_token: str, text: str) -> None:
    async with AsyncApiClient(_configuration) as api_client:
        api = AsyncMessagingApi(api_client)
        await api.reply_message(
            ReplyMessageRequest(
                reply_token=reply_token,
                messages=[TextMessage(type="text", text=text)],
            )
        )


async def push(user_id: str, text: str) -> None:
    async with AsyncApiClient(_configuration) as api_client:
        api = AsyncMessagingApi(api_client)
        await api.push_message(
            PushMessageRequest(
                to=user_id,
                messages=[TextMessage(type="text", text=text)],
            )
        )


async def get_display_name(user_id: str) -> str:
    """Fetch the LINE display name for a user ID."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            r = await client.get(
                f"https://api.line.me/v2/bot/profile/{user_id}",
                headers={"Authorization": f"Bearer {settings.line_channel_access_token}"},
            )
            if r.status_code == 200:
                return r.json().get("displayName", user_id)
    except Exception:
        pass
    return user_id
