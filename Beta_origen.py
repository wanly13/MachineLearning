import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Carga los datos desde un archivo CSV u otra fuente
data = pd.read_csv('Data.csv')

# Divide los datos en variables independientes (X) y dependientes (Y)
X = data[['Engine Size(L)']]
y = data['CO2 Emissions(g/km)']

# Crea una instancia del modelo de regresión lineal con fit_intercept=False
model = LinearRegression(fit_intercept=False)

# Entrena el modelo utilizando los datos de entrenamiento
model.fit(X, y)

# Obtiene los coeficientes del modelo
beta_0 = model.intercept_ #Aqui es 0 por partir del inicio
beta_1 = model.coef_[0] #El beta calculado que parte desde el inicio

print(f"Beta_0 (intercept): {beta_0}")
print(f"Beta_1 (slope): {beta_1}")

# Calcula las predicciones del modelo
y_pred = model.predict(X)


# Calcula el error promedio cuadrático (MSE)
#MSE = (1/n) * Σ(yi - ŷi)^2

mse = np.mean((y_pred - y) ** 2)
print(f"Mean Squared Error (MSE): {mse}")



# Visualiza los puntos de datos reales y la línea de regresión
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.legend()
plt.show()

