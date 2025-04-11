# Climate Change Impact Analyzer

## 📌 Description
This project is a Python tool designed to analyze and visualize climate data using prediction algorithms, clustering, and anomaly detection. It uses real data downloaded via the Meteostat API.

## 🔧 Requirements
- Python 3.8 or higher
- pip

### 📦 Installing Dependencies
Install all dependencies by running:

1. **Clone the Repository & Navigate to the Project Folder**
git clone <repository-url>
cd climate_change_analyzer

2. **Setup/Create a Virtual Environment**

For windows:
python -m venv venv
.\venv\Scripts\activate

For Linux/MacOS:
python3 -m venv venv
source venv/bin/activate

2. **Install required packages**
```bash
pip install -r requirements.txt
```

Content of `requirements.txt` includes:
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
├── data/                
├── htmls/               
├── src/                 
│   ├── __init__.py
│   ├── algorithms.py   
│   ├── cli.py           
│   ├── data_processor.py
│   ├── visualizer.py    
│   ├── main.py        
│   └── locations.py     
├── tests/              
├── requirements.txt     
├── README.md           
└── venv/ 

```

## 🚀 Running the Project

### 🔄 1. Download Real Data from API

```bash
python -m src.cli download
```
This will generate a file `data/climate_data_api.csv` with real data obtained from the Meteostat API. However, first it will ask for your desired location from the preexisting locations. Please select one from here.

### 📈 2. Temperature Prediction

```bash
python -m src.cli predict --data data/climate_data_api.csv```
Generates an interactive temperature trend graph (`interactive_temperature_trend.html`).

### 🔍 3. Climate Data Clustering

```bash
python -m src.cli cluster --data data/climate_data_api.csv```
Generates an interactive clustering graph (`interactive_clusters.html`).

### 🚨 4. Anomaly Detection

```bash
python -m src.cli anomalies --data data/climate_data_api.csv```
Generates an interactive anomaly detection graph (`interactive_anomalies.html`).

###  5. Interactive Menu
```bash
python src/main.py```

Use the on-screen menu to select:

    Download Real Data

    Temperature Prediction

    Clustering Analysis

    Anomaly Detection

    Exit Program



## 📑 Unit Testing
Run tests from the project root with:
```bash
python -m unittest discover tests
```


## 📋 Important Notes
- Internet Connection: Ensure you have an active internet connection when downloading data via the API.

- Interactive Graphs: Visualizations are saved as HTML files in the htmls folder and will automatically open in your default web browser.

- Location Selection: The src/locations.py file contains hardcoded locations. Adjust or expand this list as needed.

- Version Control: Refer to the accompanying git_commands.txt for common git operations when making changes.

## 💡 Authors
- Name: Antonio Fistonich
- Name: Diego Chang 
- Name: Samuel Marcano 
- Course: CIS4930, Spring 2025

