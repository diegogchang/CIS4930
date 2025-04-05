from meteostat import Stations, Daily
from datetime import datetime
import pandas as pd

class DataProcessor:
    def __init__(self, file_path: str = None):
        self.file_path = file_path
        self.df = None
        self.df_original = None  # Guarda una copia de los datos originales

    def load_data(self) -> pd.DataFrame:
        self.df = pd.read_csv(self.file_path, parse_dates=['time'])
        self.df_original = self.df.copy()  # Preserva datos originales
        return self.df

    def clean_data(self) -> pd.DataFrame:
        self.df.dropna(inplace=True)
        self.df['temperature_normalized'] = (self.df['temperature'] - self.df['temperature'].mean()) / self.df['temperature'].std()
        return self.df

    def get_features_and_target(self):
        X = self.df[['year', 'month']].values
        y = self.df['temperature_normalized'].values
        return X, y
    
    def download_data_from_api(self, start_year: int, end_year: int, lat: float, lon: float):
        """
        Descarga datos reales históricos usando Meteostat.
        """
        start = datetime(start_year, 1, 1)
        end = datetime(end_year, 12, 31)

        stations = Stations()
        stations = stations.nearby(lat, lon)
        station = stations.fetch(1)

        data = Daily(station, start, end)
        data = data.fetch().reset_index()  # <-- Aquí asegúrate que NO pierdes el índice original (que incluye fechas)

        # Guardar y formatear los datos
        data['year'] = data['time'].dt.year
        data['month'] = data['time'].dt.month
        data.rename(columns={'tavg': 'temperature'}, inplace=True)

        self.df = data[['time', 'year', 'month', 'temperature']].dropna()  # Incluimos 'time' aquí

        # Guarda en archivo CSV
        self.df.to_csv('data/climate_data_api.csv', index=False)
        print("Datos reales descargados en 'data/climate_data_api.csv'")
        return self.df




