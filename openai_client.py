from openai import OpenAI

class OpenaiClient:
    def __init__(self):
        self.client = OpenAI()

    def request_message(self, prompt):
        completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": str(prompt)}
        ]
        )
        return completion