import json
import re

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


def extract_json_objects(raw_output: str):
    try:
        # Allow outputting a JSON list directly
        if raw_output.strip().startswith("["):
            objs = json.loads(raw_output)
            return [obj for obj in objs if isinstance(obj, dict) and "query" in obj]
        else:
            matches = re.findall(r'{\s*"query":\s*".+?",\s*"tools":\s*\[.*?\]\s*}', raw_output, re.DOTALL)
            return [json.loads(m) for m in matches]
    except Exception as e:
        print("JSON parse error:", e)
        return []
