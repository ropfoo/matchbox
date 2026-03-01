from typing import TypedDict


class CountResult(TypedDict):
    count: int
    matches: list[str]
    match_counts: dict[str, int]
    unique_count: int