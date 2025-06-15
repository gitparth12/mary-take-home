# lsb: disable
from dotenv import load_dotenv

load_dotenv()

def build_prompt(n: int=2) -> str:
    prompt = f"""
You are an expert legal assistant helping build a dataset for training a language model to decide which tools to use when answering legal questions.

Your task is to:
1. Read the legal document text below.
2. Generate up to {n} realistic legal queries based on this content.
3. For each query, specify which tools to use and with what arguments.

The available tool names are:
- "full_text_search" (for exact rule, statute, and document lookups)
- "vector_search" (for vague, semantic or explanatory questions)
- You can use both tools if appropriate.

Only generate entries if the text contains meaningful legal content. If not, return nothing.

Your output must be a list of JSON objects like this:

{{
  "query": "What does Rule 4:11(e)(2) say about document authenticity?",
  "tools": [
    {{ "name": "full_text_search", "arguments": {{ "query": "Rule 4:11(e)(2) document authenticity" }} }}
  ]
}}

{{
  "query": "Why are photos important as legal evidence?",
  "tools": [
    {{ "name": "vector_search", "arguments": {{ "query": "importance of photographs in evidence" }} }}
  ]
}}

Respond only with a JSON list. If there's nothing relevant, return an empty list: `[]`

I will start attaching inputs in subsequent prompts.
"""
    return prompt.strip()

def main():
    pass

if __name__ == "__main__":
    main()
