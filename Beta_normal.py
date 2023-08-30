import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Carga los datos desde un archivo CSV u otra fuente
data = pd.read_csv('Data.csv')

# Divide los datos en variables independientes (X) y dependientes (Y)
X = data[['Engine Size(L)']]
y = data['CO2 Emissions(g/km)']

# Crea una instancia del modelo de regresión lineal
model = LinearRegression()

# Entrena el modelo utilizando los datos de entrenamiento
model.fit(X, y)

# utilizado en Y=b0+b1*x   que es la fromula de la regresion lineal
beta_0 = model.intercept_
beta_1 = model.coef_[0] 

print(f"Beta_0 (intercept): {beta_0}")
print(f"Beta_1 (slope): {beta_1}")

# Realiza predicciones en el conjunto de prueba
y_pred = model.predict(X)


# Calcula el error promedio cuadrático (MSE)
mse = np.mean((y_pred - y) ** 2)
print(f"Mean Squared Error (MSE): {mse}")


# Visualiza los puntos de datos reales y la línea de regresión
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.legend()
plt.show()
