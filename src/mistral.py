# lsp: disable
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
from helpers import extract_json_objects
import torch
import os
import json
import re

class Mistral:
    def __init__(self, model_name="mistralai/Mistral-7B-Instruct-v0.3"):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float16,
                device_map=device
                )
        self.chat_history = []

    def initialise_chat(self, prompt: str):
        self.chat_history = [
            {"role": "system", "content": prompt}
        ]


    def generate(self, prompt: str, max_tokens: int = 1024, temperature: float = 0.7) -> list[dict]:
        # Append the new document section
        self.chat_history.append({"role": "user", "content": prompt})

        prompt = self.build_chat_prompt()

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                temperature=temperature,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
        output_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extract only the newly generated part
        new_text = output_text[len(prompt):].strip()

        return extract_json_objects(new_text)


    def build_chat_prompt(self) -> str:
        prompt = ""
        for turn in self.chat_history:
            if turn["role"] == "system":
                prompt += f"<s>[INST] <<SYS>>\n{turn['content']}\n<</SYS>>\n"
            elif turn["role"] == "user":
                prompt += f"{turn['content']} [/INST] "
        return prompt.strip()
