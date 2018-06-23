from slack_event import SlackEvent
from utils import appears_in


class LunchbotMessage(SlackEvent):
    YN_YES_RESPONSE = "YN_YES_RESPONSE"
    YN_NO_RESPONSE = "YN_NO_RESPONSE"
    YN_RESPONSE_NOT_FOUND = "YN_RESPONSE_NOT_FOUND"

    positive_words = [
        "yes",
        "aye",
        "yeah"
    ]

    negative_words = [
        "no",
        "cilia"
    ]

    def get_yn_response(self):
        """Return YN_YES_RESPONSE if a "yes" is detected in the message, or YN_NO_RESPONSE for no. Otherwise, return
        YN_RESPONSE_NOT_FOUND.
        """
        text = self.get_text()
        tokens = text.lower().split()

        if any(appears_in(word, tokens) for word in self.positive_words):
            print("Affirmative response detected using complex deep neural net algorithm.")
            return self.YN_YES_RESPONSE
        elif any(appears_in(word, tokens) for word in self.negative_words):
            print("Negative response detected using complex deep neural net algorithm.")
            return self.YN_NO_RESPONSE
        else:
            return self.YN_RESPONSE_NOT_FOUND
