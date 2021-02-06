# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 02:49:06 2021

@author: enzzo
"""


import matplotlib.pyplot as plt

# Definir los Datos
x1=[0.25,1.25,2.25,3.25,4.25]
y1=[10,55,80,32,40]
x2=[0.75,1.75,2.75,3.75,4.75]
y2=[42,26,10,29,66]
# Configurar las caracteristicas del grafico
plt.scatter(x1,y1,label='Datos 1',color='red')
plt.scatter(x2,y2,label='Datos 2',color='purple')
# Definir titulo y nombres de ejes
plt.title('Grafico de Dispersion')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#Mostrar leyenda y figura
plt.legend()
plt.show()