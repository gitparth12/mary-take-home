# lsb: disable
import json
import re
from typing import Callable
from dotenv import load_dotenv
from gemini import Gemini
from mistral import Mistral
from helpers import *

_ = load_dotenv()

def main():
    gemini = Gemini()
    gemini.initialise_chat(build_prompt())
    # mistral = Mistral()
    # mistral.initialise_chat(build_prompt())
    generate_from_all_pages(gemini.generate, "data/document_ocr.txt", "data/dataset.jsonl")

if __name__ == "__main__":
    main()
