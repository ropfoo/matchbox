import re
import sys

from src.utils.count_regex_in_rtf import count_regex_in_rtf
from src.utils.get_args import get_args



def main():

    args = get_args()

    file_path = args.get('file')

    pattern = args.get('pattern')

    try:
        result = count_regex_in_rtf(pattern, file_path)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except re.error as e:
        print(f"Error: Invalid regex pattern: {e}")
        sys.exit(1)

    print(f"\nFile:    {file_path}")
    print(f"Pattern: {pattern}")
    print(f"Matches: {result['count']}\n")

if __name__ == "__main__":
    main()