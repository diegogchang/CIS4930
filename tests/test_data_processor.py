import unittest
import pandas as pd
import os
import tempfile
from src.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file with test data.
        self.test_csv = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        data = pd.DataFrame({
            'time': pd.to_datetime(['2020-01-01', '2020-02-01', '2020-03-01']),
            'year': [2020, 2020, 2020],
            'month': [1, 2, 3],
            'temperature': [10, 12, 14]
        })
        data.to_csv(self.test_csv.name, index=False)
        self.test_csv.close()
        self.processor = DataProcessor(self.test_csv.name)
    
    def tearDown(self):
        # Remove the temporary CSV file
        os.remove(self.test_csv.name)
    
    def test_load_and_clean_data(self):
        df = self.processor.load_data()
        self.assertFalse(df.empty)
        # 'temperature_normalized' should not exist before cleaning
        self.assertNotIn('temperature_normalized', df.columns)
        df_clean = self.processor.clean_data()
        self.assertIn('temperature_normalized', df_clean.columns)
    
    def test_get_features_and_target(self):
        self.processor.load_data()
        self.processor.clean_data()
        X, y = self.processor.get_features_and_target()
        # Expect two columns: 'year' and 'month'
        self.assertEqual(X.shape[1], 2)
        # Ensure that we have as many target values as rows (3 in our case)
        self.assertEqual(len(y), 3)
    
    def test_get_features_for_clustering(self):
        self.processor.load_data()
        self.processor.clean_data()
        features = self.processor.get_features_for_clustering()
        # Since we group by year and there is one year (2020), expect one row with two features: mean and std.
        self.assertEqual(features.shape[0], 1)
        self.assertEqual(features.shape[1], 2)

if __name__ == '__main__':
    unittest.main()
