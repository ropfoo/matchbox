import argparse

from src.model.args import Args


def get_args() -> Args:
    parser = argparse.ArgumentParser(
        description="Count regex occurrences in a PDF or RTF file."
    )
    parser.add_argument("file", help="Path to the file")
    parser.add_argument("--pattern", required=True, help="Regex pattern to search for")

    parsed = parser.parse_args()

    return Args(file=parsed.file, pattern=parsed.pattern)
