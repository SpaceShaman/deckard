import regex
from typing import Iterable


def extract(text: str, patterns: Iterable[str]) -> dict | None:
    combined_pattern = r"(?s)"
    for pattern in patterns:
        combined_pattern += rf"(?=.*?{pattern})"
    result = regex.search(combined_pattern, text)
    if result:
        return result.groupdict()
