import regex
from typing import Iterable


def extract(text: str, patterns: Iterable[str]) -> dict | None:
    lookaheads = "".join(rf"(?:(?=.*?{p}))?" for p in patterns)
    combined = rf"(?s)^{lookaheads}.*$"
    result = regex.search(combined, text)
    if result:
        return result.groupdict()
