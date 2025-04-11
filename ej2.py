import numpy as np
from sklearn.linear_model import LinearRegression
tamanios = np.array([50, 75, 100, 125, 150]).reshape((-1, 1))
precios_dolares = np.array([100000, 150000, 200000, 250000, 300000])

tipo_cambio = 18
precios_pesos = precios_dolares * tipo_cambio

modelo = LinearRegression()
modelo.fit(tamanios, precios_pesos)
precio_predicho = modelo.predict(np.array([[110]]))
print(f"Precio predicho en pesos mexicanos: {precio_predicho[0]:,.2f}")