import os

import requests

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class PushNotificationInput(BaseModel):
    """Input schema for PushNotificationTool."""
    message: str = Field(..., description="The message to send.")

class PushNotificationTool(BaseTool):
    name: str = "Send Push Notification"
    description: str = (
        "Tool to send push notifications to users"
    )
    args_schema: Type[BaseModel] = PushNotificationInput

    def _run(self, message: str) -> str:
        pushover_user = os.getenv("PUSHOVER_USER")
        pushover_token = os.getenv("PUSHOVER_TOKEN")
        pushover_url = "https://api.pushover.net/1/messages.json"

        print(f"Push: {message}")
        payload = {
            "token": pushover_token,
            "user": pushover_user,
            "message": message
        }
        requests.post(pushover_url, data=payload)
        return '{"notification": "sent"}'