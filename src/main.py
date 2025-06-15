# lsp: disable

# AI generated keywords and templates
FULL_TEXT_KEYWORDS = [
    "rule", "statute", "code", "admit", "deny", "filed", "date", "document", "court", "number", "form", "definition"
]
VECTOR_SEARCH_KEYWORDS = [
    "meaning", "reason", "explain", "why", "describe", "difference", "summary", "case", "example", "impact"
]

TEMPLATES = [
    "What does the {} say?",
    "Explain the purpose of {}.",
    "Summarize the legal basis for {}.",
    "What is the difference between {} and {}?",
    "When is {} typically used in court filings?",
    "Which rule governs {}?",
    "Why is {} important in litigation?",
    "What is required for {} to be valid?",
    "List documents related to {}.",
    "Give precedent cases involving {}.",
]

# General Plan
# - Given 400 something pages, simplify approach to one entry per page
# For each page, look for full text or vector search keywords
# Choose one of the found ones (or skip current page if none found)
# Use one of the templates to insert text based on the keyword found
# Might have to look into some traditional NLP to accomplish this
