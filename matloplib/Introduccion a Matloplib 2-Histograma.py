# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 02:44:43 2021

@author: enzzo
"""

import matplotlib.pyplot as plt

# Definir los Datos
a=[22,55,62,45,21,22,34,42,42,4,2,102,95,85,110,120,
   70,65,55,111,115,80,75,65,44,43,42,48]
bins=[0,10,20,30,40,50,60,70,80,90,100]

# Configurar las caracteristicas del grafico
plt.hist(a,bins,histtype='bar',rwidth=0.8,color='lightgreen')
# Definir titulo y nombres de ejes
plt.title('Histograma')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#Mostrar figura
plt.show()
