import json

from backend.services.gemini_service import model


def review_code(diff: str):

    prompt = f"""
You are a senior software engineer reviewing a pull request.

Review the git diff.

IMPORTANT:

- Do NOT assume business requirements.
- Do NOT invent bugs.
- Only report observations visible from the code changes.
- Focus on developer-relevant feedback.

Return ONLY valid JSON.

{{
    "code_smells": [],
    "performance_observations": [],
    "security_observations": [],
    "maintainability_feedback": [],
    "transactional_risks": [],
    "testing_suggestions": []
}}

Git Diff:

{diff}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return json.loads(text)