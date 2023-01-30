# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:40:49 2019

@author: Bolsista
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import epsilon_0

def Phi(x,y):
    q1 = 1; q2 = -1
    x1 = 5; y1 = 0
    x2 = -5; y2 = 0
    d1 = np.sqrt((x - x1)**2 + (y - y1)**2)
    d2 = np.sqrt((x - x2)**2 + (y - y2)**2)
    const = 1/(4*np.pi*epsilon_0)
    
    return const*(q1/d1 + q2/d2)

def dx(x, y):
    return (Phi(x + h/2, y) - Phi(x - h/2, y))/h

def dy(x, y):
    return (Phi(x, y + h/2) - Phi(x, y - h/2))/h

h = 1e6
x = np.linspace(-25, 25, 100)
y = np.linspace(-25, 25, 100)
M = np.zeros([100,100], float)

for i in range(0, np.size(x)):
    for j in range(0, np.size(y)):    
        M[i, j] = Phi(x[i], y[j])
        
plt.imshow(M, vmin =-1e9, vmax = 1e9, cmap = "hot")
plt.title("Potencial de um Dipolo Elétrico")
plt.colorbar()
plt.show()


E = np.zeros([100,100], float)
Theta = np.zeros([100,100], float)

for l in range(0,np.size(x)):
    for m in range(0, np.size(y)):
        Ex = -dx(x[l], y[m])
        Ey = -dy(x[l], y[m])
        E[l, m] = np.sqrt(((Ex)**2 + (Ey)**2))
        Theta[l,m] = np.arctan(Ey/Ex)

plt.imshow(E, cmap = "inferno")
plt.title("Campo Elétrico de um Dipolo")
plt.colorbar()
plt.show()
plt.imshow(Theta, cmap = "hsv")
plt.colorbar()
plt.show()
         