import unittest
from unittest.mock import patch, MagicMock
from src.utils.count_regex_in_pdf import count_regex_in_pdf

class TestCountRegexInPdf(unittest.TestCase):

    @patch("src.utils.count_regex_in_pdf.PdfReader")
    def test_count_regex_in_pdf_single_match(self, mock_pdf_reader):
        # Setup mock for PdfReader
        mock_page = MagicMock()
        mock_page.extract_text.return_value = "Hello world!"
        mock_reader_instance = mock_pdf_reader.return_value
        mock_reader_instance.pages = [mock_page]

        regex = "Hello"
        expected_result = {
            'count': 1,
            'matches': ['Hello'],
            'match_counts': {'Hello': 1},
            'unique_count': 1,
        }

        result = count_regex_in_pdf(regex, "dummy.pdf")

        self.assertEqual(result['count'], expected_result['count'])
        self.assertEqual(result['matches'], expected_result['matches'])
        self.assertEqual(result['match_counts'], expected_result['match_counts'])
        self.assertEqual(result['unique_count'], expected_result['unique_count'])

    @patch("src.utils.count_regex_in_pdf.PdfReader")
    def test_count_regex_in_pdf_multiple_matches(self, mock_pdf_reader):
        # Setup mock for PdfReader with multiple pages
        mock_page1 = MagicMock()
        mock_page1.extract_text.return_value = "the quick brown fox"
        mock_page2 = MagicMock()
        mock_page2.extract_text.return_value = "jumps over the lazy dog"
        
        mock_reader_instance = mock_pdf_reader.return_value
        mock_reader_instance.pages = [mock_page1, mock_page2]

        regex = "the"
        expected_result = {
            'count': 2,
            'matches': ['the', 'the'],
            'match_counts': {'the': 2},
            'unique_count': 1,
        }

        result = count_regex_in_pdf(regex, "dummy.pdf")

        self.assertEqual(result['count'], expected_result['count'])
        self.assertEqual(result['matches'], expected_result['matches'])
        self.assertEqual(result['match_counts'], expected_result['match_counts'])
        self.assertEqual(result['unique_count'], expected_result['unique_count'])

if __name__ == '__main__':
    unittest.main()
