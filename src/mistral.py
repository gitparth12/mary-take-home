# lsp: disable
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
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
