import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Carga los datos desde un archivo CSV u otra fuente
data = pd.read_csv('Data.csv')

# Divide los datos en variables independientes (X) y dependientes (y)
X = data[['Engine Size(L)']]
y = data['CO2 Emissions(g/km)']

num_iterations = 100
beta_non_origin_sum = 0

#beta desde el inicio de la data
for i in range(num_iterations):
    # Selecciona índices aleatorios para excluir un punto de datos
    indices_to_exclude = np.random.choice(len(X), size=1, replace=False)
    
    # Crea nuevas matrices X y y sin los puntos de datos seleccionados
    X_sample = X.drop(indices_to_exclude)
    y_sample = y.drop(indices_to_exclude)
    
    # Regresión lineal convencional
    model_non_origin = LinearRegression()
    model_non_origin.fit(X_sample, y_sample)
    beta_non_origin_sum += model_non_origin.coef_[0]

# Calcula el promedio del coeficiente beta
Beta_prom = beta_non_origin_sum / num_iterations

print("β promedio (sin pasar por el origen): ",Beta_prom)

beta_origen=0

for i in range(num_iterations):
    # Selecciona índices aleatorios para excluir un punto de datos
    indices_to_exclude = np.random.choice(len(X), size=1, replace=False)
    
    # Crea nuevas matrices X y y sin los puntos de datos seleccionados
    X_sample = X.drop(indices_to_exclude)
    y_sample = y.drop(indices_to_exclude)
    
    # Regresión lineal desde el origen
    model_origin = LinearRegression(fit_intercept=False)
    model_origin.fit(X_sample, y_sample)
    beta_origen += model_origin.coef_[0]

beta_prom_origen= beta_origen / num_iterations


print("β promedio (sin pasar por el origen): ",beta_prom_origen)

