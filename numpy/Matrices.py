# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 02:58:47 2021

@author: enzzo
"""
import numpy as np

# Crear una Matriz de unos - 3 filas 4 columnas
print("Matriz de unos - 3 filas 4 columnas")
unos = np.ones((3,4)) 
print(unos)
print() 

# Crear una matriz de ceros - 3 filas 4 columnas
print("Matriz de ceros - 3 filas 4 columnas")
ceros=np.zeros((3,4))
print(ceros)
print()

# Crear una Matriz de numeros aleatorios - 2 filas 2 columnas
print("Matriz de numeros aleatorios - 2 filas 2 columnas")
aleatorios =np.random.random((2,2))
print(aleatorios)
print()

# Crear una Matriz Vacia
print("Matriz Vacia")
vacia = np.empty((3,2))
print(vacia)
print()

#Crear una Matrix que contenga un unico valor en todas las posiciones
print("Matriz de un solo valor")
full = np.full((2,2),5)
print(full)
print()

#Crear matrices con valores espacidos uniformemente
print("Matrices con valores espacidos uniformemente")
espacio1=np.arange(0,30,5)
print(espacio1)

espacio2 =np.linspace(0,2,5)
print(espacio2)

print()

#Crear Matriz Identidad
print("Matrices Identidad")
identidad1 = np.eye(4,4)
print(identidad1)
print()
identidad2=np.identity(4)
print(identidad2)
print()

                        #Insepccionar Matrices

#Conocer las dimensiones de una matriz
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)
print()

#conocer el tipo de los datos
a= np.array([(1,2,3)])
print(a.dtype)
print()

# Conocer el tamanño y la forma de la matriz 
a= np.array([(1,2,3,4,5,6)])
print(a.size)
print()
print(a.shape)
print()

# Cambio de tamaño y forma de las matrices 
a=np.array([(8,9,10),(11,12,13)])
print(a)
print()
a=a.reshape(3,2)
print(a)
print()

#Extraer un solo valor de la matriz - el valor ubicado en la fila 0 columna 2
a= np.array([(1,2,3,4),(3,4,5,6)])
print(a[0,2])
print()

#Extraer los valores de todas las filas ubicados en la columna 3
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a[0:,2])
print()

#Operaciones entre Matrices 

#Encontrar el minimo, maximo y la suma
a=np.array([2,4,8])
print(a.min())
print(a.max())
print(a.sum())
print()

# Calcular la raiz cuadrada y la desviacion estandar
a=np.array([(1,2,3),(3,4,5)])
print(np.sqrt(a))
print(np.std(a))
print()

# Calcular la suma, resta, multiplicacion y division de dos matrices
x=np.array([(1,2,3),(3,4,5)])
y=np.array([(1,2,3),(3,4,5)])
print(x+y)
print(x-y)
print(x*y)
print(x/y)
