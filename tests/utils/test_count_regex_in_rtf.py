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
            'match_counts': {'Hello': 1},
            'unique_count': 1,
        }

        with patch("builtins.open", mock_open(read_data=rtf_content)):
            result = count_regex_in_rtf(regex, "dummy.rtf")

        self.assertEqual(result['count'], expected_result['count'])
        self.assertEqual(result['matches'], expected_result['matches'])
        self.assertEqual(result['match_counts'], expected_result['match_counts'])
        self.assertEqual(result['unique_count'], expected_result['unique_count'])

    def test_count_regex_in_rtf_multiple_matches(self):
        rtf_content = "the quick brown fox jumps over the lazy dog"
        regex = "the"
        expected_result = {
            'count': 2,
            'matches': ['the', 'the'],
            'match_counts': {'the': 2},
            'unique_count': 1,
        }

        with patch("builtins.open", mock_open(read_data=rtf_content)):
            result = count_regex_in_rtf(regex, "dummy.rtf")

        self.assertEqual(result['count'], expected_result['count'])
        self.assertEqual(result['matches'], expected_result['matches'])
        self.assertEqual(result['match_counts'], expected_result['match_counts'])
        self.assertEqual(result['unique_count'], expected_result['unique_count'])

    def test_count_regex_in_rtf_no_match(self):
        rtf_content = "hello world"
        regex = "python"
        expected_result = {
            'count': 0,
            'matches': [],
            'match_counts': {},
            'unique_count': 0,
        }

        with patch("builtins.open", mock_open(read_data=rtf_content)):
            result = count_regex_in_rtf(regex, "dummy.rtf")

        self.assertEqual(result['count'], expected_result['count'])
        self.assertEqual(result['matches'], expected_result['matches'])
        self.assertEqual(result['match_counts'], expected_result['match_counts'])
        self.assertEqual(result['unique_count'], expected_result['unique_count'])

    def test_count_regex_in_rtf_regex_pattern(self):
        rtf_content = "Matches: 123, 456, 789, 123"
        regex = r"\d+"
        expected_result = {
            'count': 4,
            'matches': ['123', '456', '789', '123'],
            'match_counts': {'123': 2, '456': 1, '789': 1},
            'unique_count': 3,
        }

        with patch("builtins.open", mock_open(read_data=rtf_content)):
            result = count_regex_in_rtf(regex, "dummy.rtf")

        self.assertEqual(result['count'], expected_result['count'])
        self.assertEqual(result['matches'], expected_result['matches'])
        self.assertEqual(result['match_counts'], expected_result['match_counts'])
        self.assertEqual(result['unique_count'], expected_result['unique_count'])


    def test_count_regex_in_rtf_with_slashes(self):
        rtf_content = "Hello world"
        regex = "/Hello/"
        expected_result = {
            'count': 1,
            'matches': ['Hello'],
            'match_counts': {'Hello': 1},
            'unique_count': 1,
        }

        with patch("builtins.open", mock_open(read_data=rtf_content)):
            result = count_regex_in_rtf(regex, "dummy.rtf")

        self.assertEqual(result['count'], expected_result['count'])
        self.assertEqual(result['matches'], expected_result['matches'])
        self.assertEqual(result['match_counts'], expected_result['match_counts'])
        self.assertEqual(result['unique_count'], expected_result['unique_count'])

    def test_count_regex_in_rtf_multiline(self):
        rtf_content = "1234\nabcd\n5678"
        regex = "^[0-9]{4}$"
        expected_result = {
            'count': 2,
            'matches': ['1234', '5678'],
            'match_counts': {'1234': 1, '5678': 1},
            'unique_count': 2,
        }

        with patch("builtins.open", mock_open(read_data=rtf_content)):
            result = count_regex_in_rtf(regex, "dummy.rtf")

        self.assertEqual(result['count'], expected_result['count'])
        self.assertEqual(result['matches'], expected_result['matches'])
        self.assertEqual(result['match_counts'], expected_result['match_counts'])
        self.assertEqual(result['unique_count'], expected_result['unique_count'])


if __name__ == '__main__':
    unittest.main()
