class LinkSend:

    WELCOME_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Notion App URL"
            ),
        },
    }


    def __init__(self, channel, text):
        self.channel = channel
        self.username = "pythonboardingbot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.text = text

    def get_message_payload(self):
            return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
             self.WELCOME_BLOCK,
             *self._render_text()
             ],
             }

    def _render_text(self):
        new_text = self.text.replace("https", "notion")
        return self._strip_text(new_text)

    @staticmethod
    def _strip_text(text):
        return [
            {"type": "section", "text": {"type": "mrkdwn", "text": text}}
        ]

