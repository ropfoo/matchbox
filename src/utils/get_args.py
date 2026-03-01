import argparse

from src.model.args import Args


def get_args() -> Args:
    parser = argparse.ArgumentParser(
        description="Count regex occurrences in an RTF or PDF file."
    )

    parser.add_argument("file", help="Path to the RTF or PDF file")

    parser.add_argument("pattern", help="Regex pattern to search for")

    parsed_args = parser.parse_args()

    args = Args(**vars(parsed_args))

    return args