import argparse
from src.data_processor import DataProcessor
from src.algorithms import TemperaturePredictor, custom_clustering, detect_anomalies
from src.visualizer import Visualizer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['predict', 'cluster', 'anomalies', 'download'])

    parser.add_argument('--data', required=False)
    parser.add_argument('--mode', choices=['normalized', 'original'], default='normalized')
    parser.add_argument('--data', required=False)  # <-- cambia aquí a required=False
    #implementation of arguments
    parser.add_argument('--data', required=False)
    parser.add_argument('--start-year', type = int, default=2000) #hello
    parser.add_argument('--end-year', type = int, default=2024)
    parser.add_argument('--lon', type = int, default=25.7617)
    parser.add_argument('--lat', type = int, default=-80.1918)
    
    
    args = parser.parse_args()

    # Si la acción es 'download', no se debe intentar cargar un archivo de datos
    if args.action == 'download':
        processor = DataProcessor()  # No le pasamos ningún archivo porque vamos a descargarlo
        processor.download_data_from_api(
            start_year=2000,
            end_year=2024,
            lat=25.7617,
            lon=-80.1918
        )
        return  # Termina aquí la ejecución si es 'download'

    if not args.data:
        parser.error("--data es requerido para esta acción.")

    processor = DataProcessor(args.data)
    processor.load_data()  # Solo se ejecuta si no estamos descargando datos

    if args.action == 'predict':
        processor.clean_data()
        X, y = processor.get_features_and_target()
        model = TemperaturePredictor()
        model.fit(X, y)
        predictions = model.predict(X)
        Visualizer.interactive_temperature_trend(processor.df['year'], y, predictions)

    elif args.action == 'cluster':
        processor.clean_data()
        X_cluster = processor.get_features_for_clustering()
        labels = custom_clustering(X_cluster, n_clusters=3)
        Visualizer.interactive_clusters(X_cluster, labels)

    elif args.action == 'anomalies':
        if args.mode == 'normalized':
            processor.clean_data()
            anomalies = detect_anomalies(processor.df['temperature_normalized'].values)
            Visualizer.interactive_anomalies(
                processor.df['temperature_normalized'].values,
                anomalies,
                processor.df['time'],
                mode='normalized'
            )
        elif args.mode == 'original':
            y_original = processor.df['temperature'].values
            anomalies = detect_anomalies(y_original)
            Visualizer.interactive_anomalies(
                y_original,
                anomalies,
                processor.df['time'],
                mode='original'
            )

if __name__ == '__main__':
    main()
