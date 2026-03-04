import re
import sys
import os

from src.utils.count_regex_in_pdf import count_regex_in_pdf
from src.utils.count_regex_in_rtf import count_regex_in_rtf
from src.utils.get_args import get_args


def main():
    args = get_args()
    file_path = args.get('file')
    pattern = args.get('pattern')

    try:
        if os.path.splitext(file_path)[1].lower() == '.rtf':
            result = count_regex_in_rtf(pattern, file_path)
        else:
            result = count_regex_in_pdf(pattern, file_path)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except re.error as e:
        print(f"Error: Invalid regex pattern: {e}")
        sys.exit(1)

    print(f"\nFile:    {file_path}")
    print(f"Pattern: {pattern}")
    print("-" * 20)
    for match, count in result['match_counts'].items():
        print(f"{match}: {count}")
    print("-" * 20)
    print(f"Unique Matches: {result['unique_count']}")
    print(f"Total Matches:  {result['count']}\n")


if __name__ == "__main__":
    main()
