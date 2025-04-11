import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#adding src path. Python didn't recognize src folder to find file main.py


from src.data_processor import DataProcessor
from src.algorithms import TemperaturePredictor, custom_clustering, detect_anomalies
from src.visualizer import Visualizer

# Fixed path to the climate data
DATA_PATH = os.path.join('data', 'climate_data_api.csv')

def run_analysis(action):
    processor = DataProcessor(DATA_PATH)

    processor.load_data()
    processor.clean_data()
    X, y = processor.get_features_and_target()

    if action == 'predict':
        print("Running temperature prediction...")
        model = TemperaturePredictor()
        model.fit(X, y)
        predictions = model.predict(X)
        Visualizer.interactive_temperature_trend(processor.df['year'], y, predictions)

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
        print("1. Predict Temperature Trends")
        print("2. Cluster Regions by Climate Patterns")
        print("3. Detect Climate Anomalies")
        print("4. Exit Program")

        choice = input("Enter your choice (1-4): ").strip()

        action_map = {
            "1": "predict",
            "2": "cluster",
            "3": "anomalies",
            "4": "exit"
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
    parser.add_argument("--action", type=str, choices=["predict", "cluster", "anomalies"],
                        help="Run a specific analysis without interactive menu.")
    args = parser.parse_args()

    if args.action:
        run_analysis(args.action)
    else:
        interactive_input()

