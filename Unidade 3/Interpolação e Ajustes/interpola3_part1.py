# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:23:49 2019

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

def lagrange(xp, yp, x): # somatório y(x)
    G = 0
    for i in range(len(xp)):
        G += yp[i]*lamb(x, xp, i)
    return G

x = np.linspace(0, 200, 200)
y = lagrange(xd,yd,x)

plt.plot(x, y, label = 'Interpolação', color='orange')
plt.scatter(xd, yd, label="Pontos experimentais", color='black')
plt.legend()
plt.title("Espalhamento de nêutrons")
plt.xlabel("Energia (MeV)")
plt.ylabel("Seção Transversal")
plt.show()