"""Core Fallacy Scanner implementation."""
import re
from typing import List, Dict, Any

class FallacyMatch:
    def __init__(self, fallacy_type: str, matched_text: str, explanation: str):
        self.fallacy_type = fallacy_type
        self.matched_text = matched_text
        self.explanation = explanation

class FallacyScanner:
    PATTERNS = [
        ("false_dilemma", re.compile(r"(either.+?or|with us or against us)", re.IGNORECASE),
         "Presents two alternatives as the only possibilities when more exist."),
        ("hasty_generalization", re.compile(r"(proves that all|always happens because|everyone knows that all)", re.IGNORECASE),
         "Draws an absolute conclusion from insufficient or singular evidence."),
        ("ad_hominem", re.compile(r"(incompetent so their point is invalid|you are stupid thus)", re.IGNORECASE),
         "Attacks the character rather than the substantive argument.")
    ]

    @classmethod
    def scan(cls, text: str) -> List[FallacyMatch]:
        matches = []
        for f_type, pattern, expl in cls.PATTERNS:
            for m in pattern.finditer(text):
                matches.append(FallacyMatch(f_type, m.group(0), expl))
        return matches
