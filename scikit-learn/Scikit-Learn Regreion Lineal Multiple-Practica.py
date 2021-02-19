# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 00:53:59 2021

@author: enzzo
"""

#REGRESION LINEAL MULTIPLE

#Importar las librerias 

from sklearn import datasets, linear_model

#Preparamos la data

## importamos los datos de la misma lirbreia de scikit-learn
boston = datasets.load_boston()
print(boston)
print()

# entendimiento de los datos

## Verifico la informacion contenida en el dataset
print("informacion contenida en el dataset:")
print(boston.keys())
print()

##Verifico las caracteristicas del dataset
print("caracteristicas del dataset")
print(boston.DESCR)
print()

##Verifico la cantidad de datos que hay en el dataset
print('Cantidad de datos')
print(boston.data.shape)
print()

##Verifico la informacion de las columnas 
print("Nombres de las columnas")
print(boston.feature_names)
print()

#Preparar la data para la regresion lineal multiple

##Seleccionamos las columnas 5, 6 y 7 del dataset
X_multiple = boston.data[:, 5:8]
print(X_multiple)
print()

##defino los datos correspondientes a las etiquetas
y_multiple = boston.target


#Implementacion de Regresion Lineal Multiple
from sklearn.model_selection import train_test_split

# Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, y_train, y_test = train_test_split(X_multiple, y_multiple, test_size = 0.2)

## defino el algoritmo a utilizar
lr_multiple = linear_model.LinearRegression()

## entreno el modelo
lr_multiple.fit(X_train, y_train)

## realizo una prediccion
y_pred_multiple = lr_multiple.predict(X_test)

print('DATOS DEL MODELO REGRESION LINEAL MULTIPLE')
print()

print("Valor de las pendientes o coeficientes 'a'")
print(lr_multiple.coef_)
print()

print("Valor de la interseccion o coeficientes 'b'")
print(lr_multiple.intercept_)
print()

print("Precision del modelo")
print(lr_multiple.score(X_train, y_train))
print()
