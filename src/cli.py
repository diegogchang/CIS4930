import argparse
from src.data_processor import DataProcessor
from src.algorithms import TemperaturePredictor, custom_clustering, detect_anomalies
from src.visualizer import Visualizer
import sys

def main():
    # Argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['predict', 'cluster', 'anomalies', 'exit'])  # Changed 'download' to 'exit'
    # Default value for --data argument, no need for user input
    parser.add_argument('--data', default="data/climate_data_api.csv", help="Path to the climate data CSV file")
    args = parser.parse_args()

    # Initialize the DataProcessor with the provided or default data file
    processor = DataProcessor(args.data)

    if args.action == 'exit':  # Exit the program
        print("Exiting the program. Goodbye!")
        sys.exit()

    # Load and clean the data for other actions
    processor.load_data()
    processor.clean_data()
    X, y = processor.get_features_and_target()

    # Action-based logic
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
