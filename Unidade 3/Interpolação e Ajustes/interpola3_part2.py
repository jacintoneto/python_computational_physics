# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:01:43 2019

@author: Bolsista
"""

import numpy as np
import matplotlib.pyplot as plt

Dados = np.loadtxt('scattering.data', float)
xd = Dados[:,0]
yd = Dados[:,1]

def lamb(x, xp, i): # produtório lambda
    l = 1
    for j in range(len(xp)):
        if(j != i):
            l *= (x -xp[j])/(xp[i] - xp[j])
    return l

n = 3 # número de pontos
o = n - 1 # ordem do polinômio
t = 4 # combinações de pontos
j = 0
for i in range(t):
    sx = xd[j:j+n]; sy = yd[j:j+n]
    a = sx[0]; b = sx[2]
    xvec = np.linspace(a, b, 200) # domínio limitante de x
    yvec = np.zeros(xvec.size, float) # imagem limitante de y
    for k in range(xvec.size): # roda xvec
        G = 0
        for l in range(len(sx)):
                G += sy[l]*lamb(xvec[k], sx, l)
        yvec[k] = G
    plt.plot(xvec, yvec, color = 'orange')
    j += 2
plt.scatter(xd, yd, label="Pontos experimentais", color='black')
plt.legend()
plt.title("Interpolação de Espalhamento de Nêutrons")
plt.xlabel("Energia (MeV)")
plt.ylabel("Seção Transversal")
plt.show()
