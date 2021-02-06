# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 02:59:39 2021

@author: enzzo
"""
"""


from sklearn import linear_model

x_entrenamiento = variablesIndependientes_entrenamiento
y_entrenamiento = variablesDependientes_entrenamiento
x_prueba = variablesIndependientes_prueba
y_prueba = variablesDependientes_prueba

algoritmo = linear_model.LinearRegression()

algoritmo.fit(x_entrenamiento,y_entrenamiento)
algoritmo.predict(x_prueba)

# para conocer el valor de la pendiente-a
a= algoritmo.coef_

#para conocer el valor de la interseccion-b
b= algoritmo.intercept_

