import unittest
from unittest.mock import patch, mock_open
from src.utils.count_regex_in_rtf import count_regex_in_rtf


class TestCountRegexInRtf(unittest.TestCase):

    def test_count_regex_in_rtf_single_match(self):
        rtf_content = r"{\rtf1\ansi\deff0 {\fonttbl {\f0 Arial;}} \f0 Hello world!}"
        regex = "Hello"
        expected_result = {
            'count': 1,
            'matches': ['Hello'],
        }

        with patch("builtins.open", mock_open(read_data=rtf_content)):
            result = count_regex_in_rtf(regex, "dummy.rtf")

        self.assertEqual(result['count'], expected_result['count'])
        self.assertEqual(result['matches'], expected_result['matches'])

    def test_count_regex_in_rtf_multiple_matches(self):
        rtf_content = "the quick brown fox jumps over the lazy dog"
        regex = "the"
        expected_result = {
            'count': 2,
            'matches': ['the', 'the'],
        }

        with patch("builtins.open", mock_open(read_data=rtf_content)):
            result = count_regex_in_rtf(regex, "dummy.rtf")

        self.assertEqual(result['count'], expected_result['count'])
        self.assertEqual(result['matches'], expected_result['matches'])

    def test_count_regex_in_rtf_no_match(self):
        rtf_content = "hello world"
        regex = "python"
        expected_result = {
            'count': 0,
            'matches': [],
        }

        with patch("builtins.open", mock_open(read_data=rtf_content)):
            result = count_regex_in_rtf(regex, "dummy.rtf")

        self.assertEqual(result['count'], expected_result['count'])
        self.assertEqual(result['matches'], expected_result['matches'])

    def test_count_regex_in_rtf_regex_pattern(self):
        rtf_content = "Matches: 123, 456, 789"
        regex = r"\d+"
        expected_result = {
            'count': 3,
            'matches': ['123', '456', '789'],
        }

        with patch("builtins.open", mock_open(read_data=rtf_content)):
            result = count_regex_in_rtf(regex, "dummy.rtf")

        self.assertEqual(result['count'], expected_result['count'])
        self.assertEqual(result['matches'], expected_result['matches'])


if __name__ == '__main__':
    unittest.main()
