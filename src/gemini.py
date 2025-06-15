import os
from helpers import extract_json_objects
from google import genai
from google.genai import types

class Gemini:
    def __init__(self, model_name="models/gemini-2.5-flash-preview-05-20"):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.chat = self.client.chats.create(model=model_name)

    def initialise_chat(self, prompt: str):
        _ = self.chat.send_message(prompt)

    def generate(self, prompt: str):
        response = self.chat.send_message(prompt)
        if not response.text:
            return []
        return extract_json_objects(response.text)
