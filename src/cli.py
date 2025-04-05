import argparse
from src.data_processor import DataProcessor
from src.algorithms import TemperaturePredictor, custom_clustering, detect_anomalies
from src.visualizer import Visualizer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['predict', 'cluster', 'anomalies', 'download'])
    parser.add_argument('--data', required=False)  # <-- cambia aquí a required=False

    #implementation of arguments
    parser.add_argument('--data', required=False)
    parser.add_argument('--start-year', type = int, default=2000) #hello
    parser.add_argument('--end-year', type = int, default=2024)
    parser.add_argument('--lon', type = int, default=25.7617)
    parser.add_argument('--lat', type = int, default=-80.1918)



    args = parser.parse_args()

    processor = DataProcessor(args.data)

    if args.action == 'download':
        processor.download_data_from_api(
            start_year=2000,
            end_year=2024,
            lat=25.7617,  # Miami
            lon=-80.1918
        )
        return

    # Para otras acciones asegúrate que 'data' fue proporcionado
    if not args.data:
        parser.error("--data es requerido para esta acción.")

    processor.load_data()
    processor.clean_data()
    X, y = processor.get_features_and_target()

    if args.action == 'predict':
        model = TemperaturePredictor()
        model.fit(X, y)
        predictions = model.predict(X)
        Visualizer.interactive_temperature_trend(processor.df['year'], y, predictions)

    elif args.action == 'cluster':
        X_cluster = processor.get_features_for_clustering()
        labels = custom_clustering(X_cluster, n_clusters=3)
        Visualizer.interactive_clusters(X_cluster, labels)

    elif args.action == 'anomalies':
        anomalies = detect_anomalies(y)
        Visualizer.interactive_anomalies(y, anomalies, processor.df['time'])


if __name__ == '__main__':
    main()

