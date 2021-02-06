# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 02:51:05 2021

@author: enzzo
"""


import matplotlib.pyplot as plt

# Definir los Datos
dormir=[7,8,6,11,7]
comer=[2,3,4,3,2]
trabajar=[7,8,7,2,2]
recreacion=[8,5,7,8,13]
divisiones=[7,2,2,13]
actividades = ['Dormir','Comer','Trabajar','Recreacion']
colores = ['red','purple','blue','orange']
# Configurar las caracteristicas del grafico
plt.pie(divisiones,labels=actividades,colors=colores,startangle=90,
        shadow=True,explode=(0.1,0,0,0),autopct='%1.2f%%')
# Definir titulo y nombres de ejes
plt.title('Grafico Circular')
#Mostrar figura
plt.show()