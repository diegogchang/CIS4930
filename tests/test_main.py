import unittest
import sys
from unittest.mock import patch
from src.main import interactive_input

class TestMain(unittest.TestCase):
    def test_interactive_menu_exit(self):
        # Simulate user entering "5" to exit from the interactive menu.
        # Since "5" maps to 'exit', we expect SystemExit to be raised.
        with patch('builtins.input', side_effect=["5"]), self.assertRaises(SystemExit):
            interactive_input()

if __name__ == '__main__':
    unittest.main()
