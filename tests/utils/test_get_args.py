import unittest
from unittest.mock import patch
import sys
from src.utils.get_args import get_args


class TestGetArgs(unittest.TestCase):

    def test_get_args_success(self):
        """Test get_args with the correct number of arguments."""
        test_args = ["prog", "test.rtf", "hello"]
        with patch.object(sys, 'argv', test_args):
            args = get_args()
            self.assertEqual(args["file"], "test.rtf")
            self.assertEqual(args["pattern"], "hello")

    def test_get_args_with_pattern_option(self):
        """Test get_args with --pattern option."""
        test_args = ["prog", "test.rtf", "--pattern", "hello"]
        with patch.object(sys, 'argv', test_args):
            args = get_args()
            self.assertEqual(args["file"], "test.rtf")
            self.assertEqual(args["pattern"], "hello")

    def test_get_args_with_positional_and_pattern_option(self):
        """Test get_args with both positional and --pattern option (option should win)."""
        test_args = ["prog", "test.rtf", "positional", "--pattern", "option"]
        with patch.object(sys, 'argv', test_args):
            args = get_args()
            self.assertEqual(args["file"], "test.rtf")
            self.assertEqual(args["pattern"], "option")

    def test_get_args_missing_pattern(self):
        """Test get_args with missing pattern argument (should exit)."""
        test_args = ["prog", "test.rtf"]
        with patch.object(sys, 'argv', test_args):
            # argparse calls sys.exit(2) when it encounters errors
            with self.assertRaises(SystemExit) as cm:
                with patch('sys.stderr'):  # Suppress error message during test
                    get_args()
            self.assertEqual(cm.exception.code, 2)

    def test_get_args_missing_file_and_pattern(self):
        """Test get_args with no arguments (should exit)."""
        test_args = ["prog"]
        with patch.object(sys, 'argv', test_args):
            # argparse calls sys.exit(2) when it encounters errors
            with self.assertRaises(SystemExit) as cm:
                with patch('sys.stderr'):  # Suppress error message during test
                    get_args()
            self.assertEqual(cm.exception.code, 2)


if __name__ == '__main__':
    unittest.main()
