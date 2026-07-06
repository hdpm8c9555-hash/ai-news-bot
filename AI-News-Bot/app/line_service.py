import requests
from app.config import LINE_CHANNEL_ACCESS_TOKEN,LINE_USER_ID

def push(text):
    requests.post(
        "https://api.line.me/v2/bot/message/push",
        headers={"Authorization":"Bearer "+LINE_CHANNEL_ACCESS_TOKEN},
        json={
            "to":LINE_USER_ID,
            "messages":[{"type":"text","text":text[:5000]}]
        }
    )
