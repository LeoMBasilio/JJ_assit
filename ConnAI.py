import openai
import os

class ConnGpt:
    def __init__(self):
        self.apiKey = os.getenv("OpenAI_API_Key")

    def get_text(self, message):
        client = openai.apiKey(self.apiKey)
        response = client.chat.completions.create(
            model= "gtp-4o",
            prompt = [
                {
                    "role": "user",
                    "content" : message
                }
            ]
        )

        return response.choice[0].message

    



        