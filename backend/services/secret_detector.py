import re

PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
    "Password Assignment": r"password\s*=",
    "Token Assignment": r"token\s*=",
    "Secret Assignment": r"secret\s*="
}


def detect_secrets(diff):
    findings = []

    for name, pattern in PATTERNS.items():
        if re.search(pattern, diff, re.IGNORECASE):
            findings.append(name)

    return findings