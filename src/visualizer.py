import plotly.express as px
import plotly.graph_objects as go
import numpy as np

class Visualizer:
    @staticmethod
    def interactive_temperature_trend(years, actual, predicted):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=actual, mode='lines+markers', name='Actual'))
        fig.add_trace(go.Scatter(x=years, y=predicted, mode='lines+markers', name='Predicted'))
        fig.update_layout(title='Interactive Temperature Trend',
                          xaxis_title='Year',
                          yaxis_title='Normalized Temperature')
        fig.write_html('interactive_temperature_trend.html')
        print("Gráfica interactiva guardada en 'interactive_temperature_trend.html'")

    @staticmethod
    def interactive_clusters(X, labels):
        fig = px.scatter(x=X[:, 0], y=X[:, 1], color=labels.astype(str),
                         labels={'x':'Temperatura promedio anual','y':'Variabilidad anual'},
                         title='Interactive Clustering por patrones climáticos')
        fig.write_html('interactive_clusters.html')
        print("Gráfica interactiva guardada en 'interactive_clusters.html'")

    @staticmethod
    def interactive_anomalies(data, anomalies):
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=data, mode='lines+markers', name='Data'))
        fig.add_trace(go.Scatter(y=np.where(anomalies, data, None), mode='markers',
                                 marker=dict(color='red', size=10), name='Anomalies'))
        fig.update_layout(title='Interactive Anomaly Detection',
                          xaxis_title='Time',
                          yaxis_title='Normalized Temperature')
        fig.write_html('interactive_anomalies.html')
        print("Gráfica interactiva guardada en 'interactive_anomalies.html'")
