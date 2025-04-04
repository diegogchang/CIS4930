from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import numpy as np

class TemperaturePredictor:
    def __init__(self):
        self.model = LinearRegression()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

def custom_clustering(data: np.ndarray, n_clusters: int = 3):
    """
    Realiza clustering utilizando KMeans.
    """
    model = KMeans(n_clusters=n_clusters, random_state=42)
    labels = model.fit_predict(data)
    return labels


def detect_anomalies(data: np.ndarray, threshold: float = 2.0):
    """
    Detecta anomalías utilizando el método estadístico simple.
    """
    mean = np.mean(data)
    std = np.std(data)
    anomalies = np.abs(data - mean) > threshold * std
    return anomalies
