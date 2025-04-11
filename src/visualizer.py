import os
import webbrowser
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

class Visualizer:
    @staticmethod
    def interactive_temperature_trend(years, actual_normalized, predicted_normalized, actual_original=None):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=actual_normalized, mode='lines+markers', name='Actual (Normalized)'))
        fig.add_trace(go.Scatter(x=years, y=predicted_normalized, mode='lines+markers', name='Predicted (Normalized)'))

        if actual_original is not None:
            fig.add_trace(go.Scatter(x=years, y=actual_original, mode='lines+markers', name='Actual (Original °C)'))

        fig.update_layout(
            title='Interactive Temperature Trend',
            xaxis_title='Year',
            yaxis_title='Temperature'
        )
        
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        html_dir = os.path.join(base_dir, 'htmls')
        os.makedirs(html_dir, exist_ok=True)
        
        file_path = os.path.join(html_dir, 'interactive_temperature_trend.html')
        fig.write_html(file_path)
        print(f"Interactive graph saved at: {file_path}")
        
        webbrowser.open("file://" + file_path)

    @staticmethod
    def interactive_clusters(X, labels):
        # --- NEW: Define friendly names for each cluster ---
        cluster_names = {
            0: "Stable Cold Climate",
            1: "Moderately Variable Climate",
            2: "Stable Warm Climate"
        }

        # --- NEW: Map cluster numbers to friendly names ---
        cluster_labels_named = np.vectorize(cluster_names.get)(labels)

        # --- Modify the plot to use friendly names ---
        fig = px.scatter(
            x=X[:, 0],
            y=X[:, 1],
            color=cluster_labels_named,  # <-- now colors show "Stable Cold Climate", etc
            labels={'x': 'Average Annual Temperature', 'y': 'Annual Temperature Variability'},
            title='Interactive Clustering of Climate Patterns'
        )

        # Everything else stays the same
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        html_dir = os.path.join(base_dir, 'htmls')
        os.makedirs(html_dir, exist_ok=True)
        file_path = os.path.join(html_dir, 'interactive_region_clusters.html')
        fig.write_html(file_path)
        print(f"Interactive graph saved at: {file_path}")
        webbrowser.open("file://" + file_path)


    @staticmethod
    def interactive_anomalies(data, anomalies, dates, mode='normalized'):
        if mode == 'normalized':
            y_label = 'Temperature (Normalized)'
            title = 'Anomaly Detection (Normalized Data)'
            filename = 'interactive_anomalies_normalized.html'
        else:
            y_label = 'Temperature (°C)'
            title = 'Anomaly Detection (Original Data - °C)'
            filename = 'interactive_anomalies_original.html'
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=data, mode='lines+markers', name='Data'))
        fig.add_trace(go.Scatter(
            x=np.array(dates)[anomalies],
            y=np.array(data)[anomalies],
            mode='markers',
            marker=dict(color='red', size=10),
            name='Anomalies'
        ))
        fig.update_layout(
            title=title,
            xaxis_title='Date',
            yaxis_title=y_label
        )
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        html_dir = os.path.join(base_dir, 'htmls')
        os.makedirs(html_dir, exist_ok=True)
        file_path = os.path.join(html_dir, filename)
        fig.write_html(file_path)
        print(f"Interactive graph saved at: {file_path}")
        webbrowser.open("file://" + file_path)
