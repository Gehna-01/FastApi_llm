def summarize_prompt(text):
    return (f"""
You are a text summarization assistant.

Analyze the text and return ONLY valid JSON.

Format:
{{
    "title": "Short title of the text",
    "summary": "A concise summary in 3-4 sentences",
    "key_points": [
        "Point 1",
        "Point 2",
        "Point 3"
    ],
    "keywords": [
        "keyword1",
        "keyword2",
        "keyword3"
    ]
}}
Text:
{text}
""")
def translate_prompt(text,language):
    return(f"""Translate the following text {text} to {language}""")

def rewrite_prompt(text,tone):
    return(f"""rewrite the following text {text} in tone {tone}""")

    