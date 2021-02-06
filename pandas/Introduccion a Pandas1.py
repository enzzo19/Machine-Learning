# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 03:31:40 2021

@author: enzzo
"""

import numpy as np
import pandas as pd

# Crear un dataframe
data = np.array([['','Col1','Col2'],['Fila1',11,22],['Fila2',33,33]])
print(pd.DataFrame(data=data[1:,1:],index=data[1:,0],columns=data[0,1:]))
print()

df=pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print('DataFrame:')
print(df)
print()

# Crear una Serie
series=pd.Series({"Argentina":"Buenos Aires",
                  "Chile":"Santiago de Chile",
                  "Colombia": "Bogota",
                  "Peru": "Lima"})
print('Series:')
print(series)
print()

           # Explorar los DataFrames

#Forma del DataFrame
print("Forma del DataFrame:")
print(df.shape)
print()

#Altura del DataFrame
print("Altura del DataFrame")
print(len(df.index))
print()

#Estadisticas del Dataframe
print("Estadisticas del DataFrame: ")
print(df.describe())
print()

#Medidas de las Columnas del DataFrame
print("Medidas de las Columnas del DataFrame: ")
print(df.mean())
print()

#Correlacion del DataFrame
print("Correlacion del DataFrame: ")
print(df.corr())
print()

#Cuenta los datos del DataFrame
print("Conteo de datos del DataFrame")
print(df.count())
print()

#Valor mas alto de cada columna del DataFrame
print("Valor mas alto de cada columna del DataFrame: ")
print(df.max())
print()

#Valor mas bajo de cada columna del DataFrame
print("Valor mas bajo de cada columna del DataFrame: ")
print(df.min())
print()

#Mediana de Cada columna del DataFrame
print("Mediana de Cada columna del DataFrame")
print(df.median())
print()

#Desviacion Estandar de cada Columna del DataFrame
print('Desviacion Estandar de la Columna del DataFrame: ')
print(df.std())
print()

# Seleccion dentro de un DataFrame

#Selecciona la Primera Columna del DataFrame
print("Primera Columna del DataFrame: ")
print(df[0])
print()

#Selecciona dos Columnaa del DataFrame
print("Dos Columnas del DataFrame: ")
print(df[[0,1]])
print()

#Selecciona el valor de la PrimeraFila y la ultima Columna del DataFrame
print(" Valor de la PrimeraFila y la ultima Columna del DataFrame: ")
print(df.iloc[0][2])
print()

#Seleccionar los valores de la primera fila del DataFrame
print("valores de la primera fila del DataFrame: ")
print(df.loc[0])
print(df.iloc[0,:])


#Pandas para Machine Learning

#1 Abrir los archivos
df= pd.read_csv('train.csv')
print(df)
print()

#2 Limpieza
     # Verificar si hay datos nulos en el DataFrame
print("Datos Nulos en el DataFrame")
print(df.isnull())
print()

#Suma de datos nulos en el DataFrame
print('Suma de datos nulos en el DataFrame')
print(df.isnull().sum())
print()

"""
Una vez que tenemos una lista de los valores perdidos
nos podemos desacer de ellos con:

df.dropna() # para eliminar las filas
df.dropna(axis=1) # para eliminar las columnas

"""

# Tambien podemos rellenar los valores perdidos con otros valores

#df.fillna(x) 