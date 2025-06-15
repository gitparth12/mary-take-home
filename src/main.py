# lsb: disable
import json
import re
from typing import Callable
from dotenv import load_dotenv
from gemini import Gemini
from helpers import *

_ = load_dotenv()

def split_ocr_by_page(ocr_text: str) -> dict[int, str]:
    pages: dict[int, str] = {}
    matches = list(re.finditer(r"=== PAGE (\d+) ===\n", ocr_text))
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i+1].start() if i + 1 < len(matches) else len(ocr_text)
        page_number = int(match.group(1))
        pages[page_number] = ocr_text[start:end].strip()
    return pages


def generate_from_all_pages(llm_func, ocr_path: str, output_path: str):
    # Split the ocr text by pages
    with open(ocr_path, "r") as f:
        raw_text = f.read()
    pages = split_ocr_by_page(raw_text)

    all_rows = []
    # Go through all pages and process
    for page_num, page_text in pages.items():
        try:
            rows = llm_func(page_text)
            for row in rows:
                row["source_page"] = page_num
            all_rows.extend(rows)
        except Exception as e:
            print(f"Failed on page {page_num}: {e}")

    # Save to JSONL
    with open(output_path, "w") as out:
        for row in all_rows:
            json.dump(row, out)
            out.write("\n")
    print(f"Generated {len(all_rows)} rows across {len(pages)} pages.")


def main():
    gemini = Gemini()
    gemini.initialise_chat(build_prompt())
    generate_from_all_pages(gemini.generate, "data/document_ocr.txt", "data/dataset.jsonl")

if __name__ == "__main__":
    main()
