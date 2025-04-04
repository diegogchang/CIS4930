# import pandas as pd
# import numpy as np

# # Crear datos sintéticos simples
# np.random.seed(42)
# years = np.repeat(np.arange(2000, 2025), 12)  # Años 2000-2024
# months = np.tile(np.arange(1, 13), 25)        # Meses de enero a diciembre repetidos
# temperatures = 20 + 0.05 * (years - 2000) + np.random.randn(len(years))

# # Crear DataFrame
# df = pd.DataFrame({
#     'year': years,
#     'month': months,
#     'temperature': temperatures
# })

# # Guardar a CSV
# df.to_csv('data/climate_data.csv', index=False)
