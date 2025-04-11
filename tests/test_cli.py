import unittest
import tempfile
import os
import sys
from unittest.mock import patch
import pandas as pd
from src.cli import main

class TestCLI(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file with minimal data
        self.test_csv = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        data = pd.DataFrame({
            'time': pd.to_datetime(['2020-01-01', '2020-02-01']),
            'year': [2020, 2020],
            'month': [1, 2],
            'temperature': [10, 12]
        })
        data.to_csv(self.test_csv.name, index=False)
        self.test_csv.close()
    
    def tearDown(self):
        os.remove(self.test_csv.name)
    
    def test_cli_exit(self):
        # Test that when action 'exit' is provided, the CLI calls sys.exit
        test_args = ['cli.py', 'exit']
        with patch.object(sys, 'argv', test_args), self.assertRaises(SystemExit):
            main()
    
    def test_cli_predict(self):
        # Test that the CLI predict action runs without error using the temporary CSV.
        # Patch webbrowser.open directly.
        test_args = ['cli.py', 'predict', '--data', self.test_csv.name]
        with patch.object(sys, 'argv', test_args), patch('webbrowser.open', lambda url: None):
            try:
                main()
            except Exception as e:
                self.fail(f"CLI predict action failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()
