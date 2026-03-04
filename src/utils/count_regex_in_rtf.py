from striprtf.striprtf import rtf_to_text

from .count_regex import count_regex
from ..model.count_result import CountResult


def count_regex_in_rtf(regex, rtf_file) -> CountResult:
    with open(rtf_file, 'r', encoding='utf-8', errors='ignore') as f:
        text = rtf_to_text(f.read())

    return count_regex(regex, text)
