# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:58:57 2019

@author: Jacinto Paulo
Professor: Leonardo Machado
Disciplina: Física Computacional I
Lista 9 - Problema 3

"""
import pylab as pl
from numpy import array, arange

# Parâmetros e condições iniciais

time_a = 0
time_b = 50
sigma = 10; erre = 28; b = 8/3
N = 10000

def f(r):#,t): # essa equação não dependende do tempo explicitamente
    x = r[0]
    y = r[1]
    z = r[2]
    fx = sigma*(y - x)
    fy = erre*x - y - x*z
    fz = x*y - b*z
    return array([fx, fy, fz], float)

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
zpoints = []
r = array([0, 1.0, 0], float)

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])
    r = RK4(r)#, t)

pl.plot(xpoints, zpoints, color = 'purple')
pl.title('Atrator Estranho de Lorenz')
pl.xlabel('$x(t)$')
pl.ylabel('$z(t)$')
pl.clf
pl.show() 
pl.plot(tpoints, ypoints, color='c')
pl.title('Solução $y(t)$')
pl.xlabel('$t$')
pl.ylabel('$y(t)$')
pl.show()