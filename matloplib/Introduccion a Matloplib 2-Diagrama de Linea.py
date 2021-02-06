# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 02:32:19 2021

@author: enzzo
"""


import matplotlib.pyplot as plt

# Definir los Datos
x1=[3,4,5,6]
y1=[5,6,3,4]
x2=[2,5,8]
y2=[3,4,3]
# Configurar las caracteristicas del grafico
plt.plot(x1,y1,label='linea 1',linewidth=4,color='blue')
plt.plot(x2,y2,label='linea 2',linewidth=4,color='green')
# Definir titulo y nombres de ejes
plt.title('Diagrama de Lineas')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#Mostrar leyenda, cuadricula y figura
plt.legend()
plt.grid()
plt.show()