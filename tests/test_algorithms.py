import unittest
import numpy as np
from src.algorithms import TemperaturePredictor, custom_clustering, detect_anomalies

class TestAlgorithms(unittest.TestCase):
    def test_temperature_predictor(self):
        # Test a simple linear relationship: y = 2*x + 1
        X = np.array([[i] for i in range(10)])
        y = 2 * X.flatten() + 1
        predictor = TemperaturePredictor()
        predictor.fit(X, y)
        predictions = predictor.predict(X)
        np.testing.assert_allclose(predictions, y, atol=1e-6)
    
    def test_custom_clustering(self):
        # Create a dataset with two obvious clusters
        data = np.array([[1, 2], [1, 1], [2, 2], [10, 10], [10, 11], [11, 10]])
        labels = custom_clustering(data, n_clusters=2)
        # Verify that there are exactly 2 unique clusters detected
        self.assertEqual(len(np.unique(labels)), 2)
    
    def test_detect_anomalies(self):
        # Create data with one clear anomaly; use threshold=1.0 so that 100 is detected as an anomaly.
        data = np.array([1, 2, 3, 100])
        anomalies = detect_anomalies(data, threshold=1.0)
        # Expect that the last element (100) is detected as an anomaly
        self.assertTrue(anomalies[-1])
        # And that the first three are not anomalies
        self.assertTrue(np.all(anomalies[:3] == False))

if __name__ == '__main__':
    unittest.main()
