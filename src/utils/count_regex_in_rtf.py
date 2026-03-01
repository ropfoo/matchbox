import re

from ..model.count_result import CountResult


def count_regex_in_rtf(regex, rtf_file) -> CountResult:
    """
    Counts the occurrences of a regex pattern in an RTF file and returns a dictionary with the count and matches.
    """

    with open(rtf_file, 'r') as file:
        raw_content = file.read()

    compile_regex = re.compile(regex)

    matches = compile_regex.findall(raw_content)

    result = CountResult(count=len(matches), matches=matches)

    print(result)

    return result
