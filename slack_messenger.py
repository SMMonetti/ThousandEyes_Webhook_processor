# Module for sending messages to slack app.
# Sergio Monetti - smonetti@cisco.com 

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import logging, sys

# Basic logging, in case API errors are encountered, when issuing requests to slack app.
logging.basicConfig(stream=sys.stderr, level=logging.WARNING)

def sendMessage(channel, message, username, icon_url, token):
    client = WebClient(token)

    try:
        response = client.chat_postMessage(channel=channel, text=message, username=username, icon_url=icon_url)

    except SlackApiError as e:
        assert e.response["ok"] is False
        assert e.response["error"]
        logging.warning(f"Got an error: {e.response}")
