import argparse
from src.data_processor import DataProcessor
from src.algorithms import TemperaturePredictor, custom_clustering, detect_anomalies
from src.visualizer import Visualizer
from src.locations import LOCATIONS
import sys

def download_data(processor):
    print("Select a location to download data:")
    # List the available locations
    locations_list = list(LOCATIONS.keys())
    for i, loc in enumerate(locations_list, 1):
        print(f"{i}. {loc}")
    choice = input("Enter the number corresponding to the location: ").strip()
    try:
        choice_idx = int(choice) - 1
        selected_loc = locations_list[choice_idx]
    except (ValueError, IndexError):
        print("❌ Invalid selection.")
        return

    lat = LOCATIONS[selected_loc]["lat"]
    lon = LOCATIONS[selected_loc]["lon"]

    # Optionally, ask for start_year and end_year, using defaults if nothing is entered.
    start_year = input("Enter start year (default 2000): ").strip()
    end_year = input("Enter end year (default 2020): ").strip()
    start_year = int(start_year) if start_year else 2000
    end_year = int(end_year) if end_year else 2020

    # Download data using the selected location and year range
    processor.download_data_from_api(start_year, end_year, lat, lon)

def main():
    # Argument parsing with a new "download" action
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['download', 'predict', 'cluster', 'anomalies', 'exit'], 
                        help="Action to perform.")
    parser.add_argument('--data', default="data/climate_data_api.csv", help="Path to the climate data CSV file")
    args = parser.parse_args()

    processor = DataProcessor(args.data)

    if args.action == 'exit':
        print("Exiting the program. Goodbye!")
        sys.exit()
    
    if args.action == 'download':
        # For download, call the helper function to select the location and download data.
        download_data(processor)
        return

    # For other actions, load and clean the data first.
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
