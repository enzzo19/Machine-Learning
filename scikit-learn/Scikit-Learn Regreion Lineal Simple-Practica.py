# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 03:42:36 2021

@author: enzzo
"""
"""
Predecir el Precio de las casa en Boston 
a partir de el numero de habitaciones que tiene la casa
"""
# LIBRERIAS A UTILIZAR
# Importamos librerias a utilizar
import numpy as np
from sklearn import datasets,linear_model
import matplotlib.pyplot as plt

# PREPARAR LA DATA
# Importamos los datos de la misma libreria de scikit-learn

boston = datasets.load_boston()
print(boston)
print()

# ENTENDIENDO LOS DATOS

# Verifico la informacion contenida en el dataset
print('Informacion en el dataset: ')
print(boston.keys())
print()

# Verifico las Caracteristicas del dataset
print('Caracteristicas del dataset')
print(boston.DESCR)
print()

# Verifico la cantidad de datos que hay en los dataset
print('Cantidad de Datos: ')
print(boston.data.shape)
print()

#Verifico la Informacion de la Columnas
print('Nombres columnas')
print(boston.feature_names)
print()

# PREPARAR LA DATA REGRESION LINEAL SIMPLE
# Seleccionamos solamente la columna 5 del dataset
X = boston.data[:, np.newaxis,5]

# Defino los datos correspondientes a las etiquetas 
y = boston.target

#Graficamos los datos correspondientes
plt.scatter(X,y)
plt.xlabel('Numero de Habitaciones')
plt.ylabel('Valor medio')
plt.show()


#IMPLEMENTACION DE REGRECSION LINEAL SIMPLE

from sklearn.model_selection import train_test_split

#Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# Definimos el algoritmo a utilizar
lr = linear_model.LinearRegression()

# Entrenamos el modelo
lr.fit(X_train,y_train)

#Realizamos la prediccion
Y_pred = lr.predict(X_test)

#Graficamos los datos junto con el modelo
plt.scatter(X_test,y_test)
plt.plot(X_test, Y_pred, color='red',linewidth=3)
plt.title("Refresion Lineal Simple")
plt.xlabel("Numero de habitaciones")
plt.ylabel("Valor medio")
plt.show()

print()
print("DATOS DEL MODELO DE RERESION LINEAL SIMPLE")
print()
print('Valor de la pendiente o coeficiente "a": ')
print(lr.coef_)
print('Valor de la pendiente o coeficiente "b": ')
print(lr.intercept_)
print("La ecuacion del modelo es: ")
print('y = ',lr.coef_,'x',lr.intercept_)
print()
print("Presicion del Modelo")
print(lr.score(X_train,y_train))

"""
En este caso el algoritmo tiene una presicion muy baja,
no quiere decir que este mal echo o no sirva,
sino que no es el mejor para este problema

"""