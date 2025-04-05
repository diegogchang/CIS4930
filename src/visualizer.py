import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os

os.makedirs('htmls', exist_ok=True)

class Visualizer:
    @staticmethod
    def interactive_temperature_trend(years, actual, predicted):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=actual, mode='lines+markers', name='Actual'))
        fig.add_trace(go.Scatter(x=years, y=predicted, mode='lines+markers', name='Predicted'))
        fig.update_layout(title='Interactive Temperature Trend',
                          xaxis_title='Year',
                          yaxis_title='Normalized Temperature')
        fig.write_html('htmls/interactive_temperature_trend.html')
        print("Gráfica interactiva guardada en 'interactive_temperature_trend.html'")

    @staticmethod
    def interactive_clusters(X, labels):
        fig = px.scatter(x=X[:, 0], y=X[:, 1], color=labels.astype(str),
                         labels={'x':'Temperatura promedio anual','y':'Variabilidad anual'},
                         title='Interactive Clustering por patrones climáticos')
        fig.write_html('htmls/interactive_clusters.html')
        print("Gráfica interactiva guardada en 'interactive_clusters.html'")

    @staticmethod
    def interactive_anomalies(data, anomalies, dates, mode='normalized'):
        if mode == 'normalized':
            y_label = 'Temperature (Normalized)'
            title = 'Anomaly Detection (Normalized Data)'
            filename = 'htmls/interactive_anomalies_normalized.html'
        else:
            y_label = 'Temperature (°C)'
            title = 'Anomaly Detection (Original Data - °C)'
            filename = 'htmls/interactive_anomalies_original.html'

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=data, mode='lines+markers', name='Data'))
        fig.add_trace(go.Scatter(x=np.array(dates)[anomalies], y=np.array(data)[anomalies],
                                mode='markers', marker=dict(color='red', size=10), name='Anomalies'))
        
        fig.update_layout(
            title=title,
            xaxis_title='Date',
            yaxis_title=y_label
        )
        
        fig.write_html(filename)
        print(f"Gráfica interactiva guardada en '{filename}'")