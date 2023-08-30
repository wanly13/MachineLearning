### No se usar readme xD


#Formula que usaremos 

Y=β0+B1*X

Donde:
Y es la variable dependiente.

X es la variable independiente.

B0 es el intercepto (punto donde la línea cruza el eje y)

​
B1 es la pendiente de la línea de regresión.









BETA_ORIGEN.PY

el valor de "beta" representará directamente la pendiente de la línea de regresión que pasa por el origen (0,0)

Cuando especificas fit_intercept=False al crear la instancia del modelo de regresión lineal, estás indicando que la línea de regresión debe pasar por el origen en lugar de tener un término de intersección.


 en la fórmula 
    y=b0+b1*x
  es el coeficiente de la pendiente de la regresión lineal. Por lo tanto, en el caso de una regresión lineal simple, el valor que necesitas es el coeficiente b1

Si estás utilizando model.coef_[0], efectivamente estás accediendo al coeficiente b1,
 que es el coeficiente de la pendiente de la línea de regresión. El término [0] se refiere al primer coeficiente en la lista de coeficientes que devuelve model.coef_, que en este caso es el coeficiente b1

En resumen, para obtener el valor del coeficiente de la pendiente b1, en una regresión lineal simple, puedes utilizar model.coef_[0].






MSE
Incluso si los valores ajustados se encuentran muy cerca de los valores reales, siempre habrá alguna diferencia residual debido a la naturaleza de los datos y la forma en que se están ajustando. Sin embargo, el MSE puede ser bastante pequeño si la regresión se ajusta bien a los datos.

En términos prácticos, un MSE muy cercano a 0 podría ser indicativo de un sobreajuste (overfitting), lo que significa que el modelo se ajusta demasiado a los datos de entrenamiento y podría no generalizar bien a nuevos datos. Por lo tanto, no necesariamente buscas un MSE de 0, sino un valor bajo que indique un buen ajuste del modelo a los datos y una capacidad razonable de generalización.



![MSE](MSE.png)

MSE = (1/n) * Σ(yi - ŷi)^2

Donde:

n es el número de puntos de datos.
yi son los valores reales de la variable dependiente.
ŷi son las predicciones del modelo para la variable dependiente correspondiente a xi.
En otras palabras, el MSE es la suma de las diferencias al cuadrado entre las predicciones del modelo y los valores reales, dividida por el número total de puntos de datos. Cuanto más bajo sea el valor del MSE, mejor será el ajuste del modelo a los datos.