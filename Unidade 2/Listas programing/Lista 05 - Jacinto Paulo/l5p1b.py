# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:11:50 2019

@author: Bolsista
"""

import numpy as np
import matplotlib.pyplot as plt

def interativo(x, xold, k):
    i=0
    
    while(abs(x - xold) >= precisao):    
        xold = x
        x = f(x, k)    
    
    raiz = x
    return raiz

def f(x, c):
    return (1 - np.exp(-c*x))

precisao = 1e-6
xold = 0
x = 1 #chute
c = np.linspace(0, 3, 300)
vecx = []

for i in c:
    valor = interativo(x, xold, i)
    vecx.append(valor)

#print(vecx)
    
plt.plot(c, vecx)
plt.title('Método de Relaxação')
plt.xlabel('c')
plt.ylabel('Raízes')

