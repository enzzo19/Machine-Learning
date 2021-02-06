# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 02:39:35 2021

@author: enzzo
"""
import matplotlib.pyplot as plt

# Definir los Datos
x1=[0.25,1.25,2.25,3.25,4.25]
y1=[10,55,80,32,40]
x2=[0.75,1.75,2.75,3.75,4.75]
y2=[42,26,10,29,66]
# Configurar las caracteristicas del grafico
plt.bar(x1,y1,label='Datos 1',width=0.5,color='lightblue')
plt.bar(x2,y2,label='Datos 2',width=0.5,color='orange')
# Definir titulo y nombres de ejes
plt.title('Grafico de Barras')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#Mostrar leyenda y figura
plt.legend()
plt.show()