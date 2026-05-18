import asyncio
import xmlrpc.client
from datetime import datetime
from enum import IntEnum
from functools import partial
from typing import Optional

from app.config import settings


class Priority(IntEnum):
    LOW = 0       # our 4-Low
    MEDIUM = 1    # our 3-Medium (default)
    HIGH = 2      # our 2-High
    CRITICAL = 3  # our 1-Critical


PRIORITY_MAP = {
    "1-Critical": Priority.CRITICAL,
    "2-High":     Priority.HIGH,
    "3-Medium":   Priority.MEDIUM,
    "4-Low":      Priority.LOW,
}

SLA_TARGETS = {
    Priority.CRITICAL: {"first_response_min": 5,  "escalate_hr": 1,  "resolution_hr": 4},
    Priority.HIGH:     {"first_response_min": 5,  "escalate_hr": 4,  "resolution_hr": 8},
    Priority.MEDIUM:   {"first_response_min": 5,  "escalate_hr": 24, "resolution_hr": 36},
    Priority.LOW:      {"first_response_min": 15, "escalate_hr": 48, "resolution_hr": 72},
}


class OdooClient:
    def __init__(self):
        self.url      = settings.odoo_url.rstrip("/")
        self.db       = settings.odoo_db
        self.username = settings.odoo_username
        self.password = settings.odoo_password
        self.team_id  = settings.odoo_helpdesk_team_id
        self._uid: Optional[int] = None
        self._common  = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")
        self._models  = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object")

    async def _run(self, fn, *args):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, partial(fn, *args))

    async def authenticate(self) -> int:
        uid = await self._run(self._common.authenticate, self.db, self.username, self.password, {})
        if not uid:
            raise RuntimeError("Odoo authentication failed — check credentials or API key")
        self._uid = uid
        return uid

    async def _call(self, model: str, method: str, args: list, kwargs: dict = None) -> any:
        if not self._uid:
            await self.authenticate()
        return await self._run(
            self._models.execute_kw,
            self.db, self._uid, self.password,
            model, method, args, kwargs or {},
        )

    async def create_ticket(
        self,
        line_user_id: str,
        line_display_name: str,
        channel_name: str,
        message: str,
        priority_label: str = "3-Medium",
    ) -> dict:
        priority = PRIORITY_MAP.get(priority_label, Priority.MEDIUM)
        sla = SLA_TARGETS[priority]
        now = datetime.utcnow()

        description = (
            f"Source: LINE\n"
            f"Channel: {channel_name}\n"
            f"LINE User ID: {line_user_id}\n"
            f"Display Name: {line_display_name}\n"
            f"Issued: {now.strftime('%Y-%m-%d %H:%M:%S')} UTC\n"
            f"Priority: {priority_label}\n"
            f"SLA - First Response: {sla['first_response_min']} min\n"
            f"SLA - Escalate by: {sla['escalate_hr']} hr\n"
            f"SLA - Resolve by: {sla['resolution_hr']} hr\n\n"
            f"Customer Message:\n{message}"
        )

        values = {
            "name": f"[LINE] {line_display_name}",
            "description": description,
            "priority": str(int(priority)),
            "team_id": self.team_id,
        }

        ticket_id = await self._call("helpdesk.ticket", "create", [values])
        return {"id": ticket_id, "priority": priority_label, "sla": sla}

    # in-memory session: line_user_id → active ticket_id
    _sessions: dict = {}

    def get_active_ticket(self, line_user_id: str) -> Optional[int]:
        return self._sessions.get(line_user_id)

    def set_active_ticket(self, line_user_id: str, ticket_id: int) -> None:
        self._sessions[line_user_id] = ticket_id

    def clear_active_ticket(self, line_user_id: str) -> None:
        self._sessions.pop(line_user_id, None)

    async def add_message_to_ticket(self, ticket_id: int, message: str) -> None:
        """Append a new customer message as a chatter note on the existing ticket."""
        await self._call(
            "helpdesk.ticket", "message_post",
            [[ticket_id]],
            {"body": f"<b>Customer (LINE):</b><br/>{message}", "message_type": "comment"},
        )

    async def update_ticket(self, ticket_id: int, values: dict) -> bool:
        return await self._call("helpdesk.ticket", "write", [[ticket_id], values])

    async def close_ticket(self, ticket_id: int) -> bool:
        """Move ticket to the first folded (done) stage."""
        stages = await self._call(
            "helpdesk.stage", "search_read",
            [[["fold", "=", True], ["team_ids", "in", [self.team_id]]]],
            {"fields": ["id"], "limit": 1, "order": "sequence asc"},
        )
        if stages:
            return await self.update_ticket(ticket_id, {"stage_id": stages[0]["id"]})
        return False

    async def close(self):
        pass


odoo = OdooClient()
