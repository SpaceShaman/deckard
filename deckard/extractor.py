import re
from typing import Iterable


def extract(text: str, patterns: Iterable[str]) -> dict | None:
    combined_pattern = r"(?s)"
    for pattern in patterns:
        combined_pattern += rf"(?=.*?{pattern})"
    pattern = re.compile(combined_pattern)
    if extracted := re.search(pattern, text):
        return _clean(extracted.groupdict())


def _clean(extracted: dict) -> dict:
    for key, value in extracted.items():
        if "phone" in key:
            extracted[key] = value.replace(" ", "")
    return extracted
