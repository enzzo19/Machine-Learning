# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 02:59:39 2021

@author: enzzo
"""

# Scikit Learn-Regresion Lineal Simple cheatshet

"""

from sklearn import linear_model #importar la libreria

x_entrenamiento = variablesIndependientes_entrenamiento
y_entrenamiento = variablesDependientes_entrenamiento
x_prueba = variablesIndependientes_prueba
y_prueba = variablesDependientes_prueba

algoritmo = linear_model.LinearRegression() # Definir el algoritmo

algoritmo.fit(x_entrenamiento,y_entrenamiento) #Entrenar el modelo
algoritmo.predict(x_prueba) #Para realizar una prediccion

# para conocer el valor de la pendiente-a
a= algoritmo.coef_

#para conocer el valor de la interseccion-b
b= algoritmo.intercept_


score(x) #Para conocer la precision del modelo
"""