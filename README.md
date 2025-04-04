# Climate Change Impact Analyzer

## 📌 Description
This project is a Python tool designed to analyze and visualize climate data using prediction algorithms, clustering, and anomaly detection. It uses real data downloaded via the Meteostat API.

## 🔧 Requirements
- Python 3.8 or higher
- pip

### 📦 Installing Dependencies
Install all dependencies by running:

```bash
pip install -r requirements.txt
```

Content of `requirements.txt` should include:
```
pandas
numpy
scikit-learn
matplotlib
seaborn
plotly
meteostat
```

## 📂 Project Structure
```
climate_change_analyzer/
│
├── data/  # Downloaded and generated data
├── src/   # Main source code
│   ├── __init__.py
│   ├── algorithms.py
│   ├── cli.py
│   ├── data_processor.py
│   ├── visualizer.py
│   └── main.py
├── tests/ # Unit tests
├── requirements.txt
├── README.md
└── venv/  # Virtual environment (optional)
```

## 🚀 Running the Project

### 🔄 1. Download Real Data from API

```bash
python -m src.cli download
```
This will generate a file `data/climate_data_api.csv` with real data obtained from the Meteostat API.

### 📈 2. Temperature Prediction

```bash
python -m src.cli predict --data data/climate_data_api.csv
```
Generates an interactive temperature trend graph (`interactive_temperature_trend.html`).

### 🔍 3. Climate Data Clustering

```bash
python -m src.cli cluster --data data/climate_data_api.csv
```
Generates an interactive clustering graph (`interactive_clusters.html`).

### 🚨 4. Anomaly Detection

```bash
python -m src.cli anomalies --data data/climate_data_api.csv
```
Generates an interactive anomaly detection graph (`interactive_anomalies.html`).


## 📑 Unit Testing
Run tests from the project root with:
```bash
python -m unittest discover tests
```


## 📋 Important Notes
- Ensure you have an internet connection to download data using the API.
- Interactive graphs are saved as HTML files and can be opened with any browser.

## 💡 Authors
- Name: Antonio Fistonich
- Name: Diego Chang 
- Name: Samuel Marcano 
- Course: CIS4930, Spring 2025

