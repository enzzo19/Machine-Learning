# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 02:46:25 2021

@author: enzzo
"""

import numpy as np
import sys
S=range(1000)
print("Resultado Lista de Python:")
print(sys.getsizeof(5)*len(S))
print()
D= np.arange(1000)
print("Resultado Numpy array: ")
print(D.size*D.itemsize)