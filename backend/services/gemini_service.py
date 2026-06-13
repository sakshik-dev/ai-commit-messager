import json
import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_commit_artifacts(diff: str):

    prompt = f"""
You are a senior software engineer.

Analyze the git diff.

Infer WHY the change was made.

Return ONLY valid JSON.

{{
    "commit_message":"",
    "pr_description":"",
    "release_notes":""
}}

Rules:

1. Use Conventional Commits.
2. Explain business intent.
3. Do not simply describe code lines.
4. Keep commit message under 72 chars.

Git Diff:

{diff}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "")

    text = text.replace("```", "").strip()

    return json.loads(text)