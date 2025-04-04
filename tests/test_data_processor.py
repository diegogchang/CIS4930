import unittest
from src.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = DataProcessor('data/climate_data.csv')
        self.processor.load_data()

    def test_clean_data(self):
        df = self.processor.clean_data()
        self.assertFalse(df.isnull().values.any())

if __name__ == '__main__':
    unittest.main()
