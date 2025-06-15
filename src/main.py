# lsb: disable
from dotenv import load_dotenv

load_dotenv()

def split_ocr_by_page(ocr_text: str) -> dict:
    pages = {}
    matches = list(re.finditer(r"=== PAGE (\d+) ===\n", ocr_text))
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i+1].start() if i + 1 < len(matches) else len(ocr_text)
        page_number = int(match.group(1))
        pages[page_number] = ocr_text[start:end].strip()
    return pages


def main():
    pass

if __name__ == "__main__":
    main()
