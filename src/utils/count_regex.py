import re
from collections import Counter

from src.model.count_result import CountResult


def count_regex(regex, text):
    if regex.startswith('/') and regex.endswith('/') and len(regex) > 1:
        regex = regex[1:-1]

    compile_regex = re.compile(regex, re.MULTILINE)
    matches = compile_regex.findall(text)

    match_counts = dict(Counter(matches))
    unique_count = len(match_counts)

    return CountResult(
        count=len(matches),
        matches=matches,
        match_counts=match_counts,
        unique_count=unique_count
    )