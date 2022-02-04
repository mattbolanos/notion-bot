import logging
# from slack_bolt import App
from slack_sdk.web import WebClient
from message import LinkSend
import os
from flask import Flask

app = Flask(__name__)

with app.app_context():
    from slack_app import slack_events_adapter

    slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
    slack_client = WebClient(slack_bot_token)

    def send_message(user_id: str, channel: str, client: WebClient, text:str):
        results = LinkSend(channel, text)

        message = results.get_message_payload()

        response = client.chat_postMessage(**message)

    @slack_events_adapter.on("message")
    def message(event, client):
 
        channel_id = event.get("channel")
        user_id = event.get("user")
        text = event.get("text")

        if text and "https://www.notion" in text.lower():
            return send_message(user_id, channel_id, client, text)

    @slack_events_adapter.on("error")
    def error_handler(err):
        print("ERROR: " + str(err))

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.run(debug=True)

# import ssl as ssl_lib
# import certifi

# ssl_context = ssl_lib.create_default_context(cafile=certifi.where())