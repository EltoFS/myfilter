import json
from myfilter.openai_client import OpenaiClient

class Myfilter:
    def __init__(self):
        self.prompt = None
        self.client = OpenaiClient()

    def home(self):
        self.prompt = "Give me a saudation without names explaining that \
            you will rewrite messages according to the selected endpoint personality"
        message = self.client.request_message(self.prompt)
        message = {
            "message": message.choices[0].message.content
        }
        return json.dumps(message)

    def gentleman(self, message):
        self.prompt = f"I want you to rewrite the following message as formal as \
            possible removing any bad words and \
            changing insults to compliments: '{message}'"
        message = self.client.request_message(self.prompt)
        message = {
            "message": message.choices[0].message.content
        }
        return json.dumps(message)
    
    def sage(self, message):
        self.prompt = f"I want you to rewrite the following message in \
            a haiku poem format: '{message}'"
        message = self.client.request_message(self.prompt)
        message = {
            "message": message.choices[0].message.content
        }
        return json.dumps(message)
