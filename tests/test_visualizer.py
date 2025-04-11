import unittest
import os
import numpy as np
import webbrowser
from src.visualizer import Visualizer

class TestVisualizer(unittest.TestCase):
    def setUp(self):
        # Override webbrowser.open to do nothing during tests.
        self.original_webbrowser_open = webbrowser.open
        webbrowser.open = lambda url: None
        # Determine the html folder path as used by Visualizer.
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.html_dir = os.path.join(base_dir, 'htmls')
        os.makedirs(self.html_dir, exist_ok=True)
    
    def tearDown(self):
        # Restore original webbrowser.open.
        webbrowser.open = self.original_webbrowser_open
        # Remove generated HTML files.
        files = ['interactive_temperature_trend.html',
                 'interactive_region_clusters.html',
                 'interactive_anomalies_normalized.html',
                 'interactive_anomalies_original.html']
        for f in files:
            file_path = os.path.join(self.html_dir, f)
            if os.path.exists(file_path):
                os.remove(file_path)
    
    def test_interactive_temperature_trend(self):
        years = np.array([2000, 2001, 2002])
        actual = np.array([0.1, 0.2, 0.3])
        predicted = np.array([0.15, 0.25, 0.35])
        Visualizer.interactive_temperature_trend(years, actual, predicted)
        file_path = os.path.join(self.html_dir, 'interactive_temperature_trend.html')
        self.assertTrue(os.path.exists(file_path))
    
    def test_interactive_clusters(self):
        X = np.array([[1, 2], [3, 4], [5, 6]])
        labels = np.array([0, 1, 0])
        Visualizer.interactive_clusters(X, labels)
        file_path = os.path.join(self.html_dir, 'interactive_region_clusters.html')
        self.assertTrue(os.path.exists(file_path))
    
    def test_interactive_anomalies_normalized(self):
        data = np.array([0.1, 0.2, 0.3])
        anomalies = np.array([False, True, False])
        dates = np.array(['2020-01-01', '2020-02-01', '2020-03-01'])
        Visualizer.interactive_anomalies(data, anomalies, dates, mode='normalized')
        file_path = os.path.join(self.html_dir, 'interactive_anomalies_normalized.html')
        self.assertTrue(os.path.exists(file_path))
    
    def test_interactive_anomalies_original(self):
        data = np.array([10, 20, 30])
        anomalies = np.array([False, True, False])
        dates = np.array(['2020-01-01', '2020-02-01', '2020-03-01'])
        Visualizer.interactive_anomalies(data, anomalies, dates, mode='original')
        file_path = os.path.join(self.html_dir, 'interactive_anomalies_original.html')
        self.assertTrue(os.path.exists(file_path))

if __name__ == '__main__':
    unittest.main()
