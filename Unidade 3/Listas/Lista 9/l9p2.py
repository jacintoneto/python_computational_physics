# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:57:57 2019

@author: Jacinto Paulo
Professor: Leonardo Machado
Disciplina: Física Computacional I
Lista 9 - Problema 2

"""

import pylab as pl
from numpy import array, arange

# Parâmetros e condições iniciais

time_a = 0
time_b = 30

alpha = 1; beta = 0.5; gamma = 0.5; delta =  2
N = 500

def f(r):#,t): # essa equação não dependende do tempo explicitamente
    x = r[0]
    y = r[1]
    fx = alpha*x - beta*x*y
    fy = gamma*x*y - delta*y
    return array([fx, fy], float)

def RK4(r):#, t):
    k1 = h*f(r)#, t)
    k2 = h*f(r+k1/2)#, t+h/2)
    k3 = h*f(r+k2/2)#, t+h/2)
    k4 = h*f(r+k3)#, t+h)
    
    return r + (1/6)*(k1+2*k2+2*k3+k4)


# Resolvendo EDO
h = (time_b - time_a)/N
tpoints = arange(time_a, time_b, h)
xpoints = []
ypoints = []
r = array([2.0, 2.0], float)

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    r = RK4(r)#, t)
    
pl.plot(tpoints, xpoints, color='c', label='$x(t)$ presas')
pl.plot(tpoints, ypoints, color='orange', label='$y(t)$ predadores')
pl.title('Modelo de Lotka–Volterra')
pl.legend()
pl.xlabel('$t$')
pl.ylabel('$x(t) \quad & \quad  y(t)$')
pl.show()

"""
A quantidade máxima de coelhos é sempre maior que a quantidade máxima que a de rapozas. Da mesma maneira,
a quantidade mínima de rapozas sempre é menor. Dessa maneira, o único momento em que a quantidade de coelhos
é menor que a de rapozas é quando a população de rapozas atinge um máximo. Devido a falta de coelhos 
(mortos pela caça e pela velhice) e morte por velhice, a população de rapozas dimunui até atingir um mínimo. 
A morte de coelhos por caça diminui e então a população volta a crescer.
"""