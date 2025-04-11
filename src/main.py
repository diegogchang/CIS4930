import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processor import DataProcessor
from src.algorithms import TemperaturePredictor, custom_clustering, detect_anomalies
from src.visualizer import Visualizer
from src.locations import LOCATIONS

# Fixed path to the climate data
DATA_PATH = os.path.join('data', 'climate_data_api.csv')

def download_data_interactive(processor):
    print("\nSelect a location to download data:")
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

    start_year = input("Enter start year (default 2000): ").strip()
    end_year = input("Enter end year (default 2020): ").strip()
    start_year = int(start_year) if start_year else 2000
    end_year = int(end_year) if end_year else 2020

    processor.download_data_from_api(start_year, end_year, lat, lon)

def run_analysis(action):
    processor = DataProcessor(DATA_PATH)

    if action == 'download':
        download_data_interactive(processor)
        return

    processor.load_data()
    processor.clean_data()
    X, y = processor.get_features_and_target()

    if action == 'predict':
        model = TemperaturePredictor()
        model.fit(X, y)
        predictions = model.predict(X)
        Visualizer.interactive_temperature_trend(
            processor.df['year'], 
            processor.df['temperature_normalized'], 
            predictions, 
            processor.df['temperature']  # <--- temperatura original
        )


    elif action == 'cluster':
        print("Running clustering analysis...")
        X_cluster = processor.get_features_for_clustering()
        labels = custom_clustering(X_cluster, n_clusters=3)
        Visualizer.interactive_clusters(X_cluster, labels)

    elif action == 'anomalies':
        print("Detecting anomalies in climate data...")
        anomalies = detect_anomalies(y)
        Visualizer.interactive_anomalies(y, anomalies, processor.df['time'])

def interactive_input():
    while True:
        print("\n🌎 Welcome to the Climate Change Impact Analyzer 🌡️")
        print("---------------------------------------------------")
        print("Select an analysis to run:")
        print("1. Download Real Data")
        print("2. Predict Temperature Trends")
        print("3. Cluster Regions by Climate Patterns")
        print("4. Detect Climate Anomalies")
        print("5. Exit Program")

        choice = input("Enter your choice (1-5): ").strip()

        action_map = {
            "1": "download",
            "2": "predict",
            "3": "cluster",
            "4": "anomalies",
            "5": "exit"
        }

        action = action_map.get(choice)

        if action == "exit":
            print("Exiting Climate Change Impact Analyzer...")
            sys.exit(0)
        elif action:
            run_analysis(action)
        else:
            print("❌ Invalid choice. Please try again.")

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Climate Change Impact Analyzer CLI")
    parser.add_argument("--action", type=str, choices=["download", "predict", "cluster", "anomalies"],
                        help="Run a specific analysis without interactive menu.")
    args = parser.parse_args()

    if args.action:
        run_analysis(args.action)
    else:
        interactive_input()
