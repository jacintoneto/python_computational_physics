# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 09:31:41 2019

@author: Jacinto Paulo
Professor: Leonardo Machado
Disciplina: Física Computacional I
Lista 10 - Problema 1

"""
import pylab as pl
from numpy import array, arange, sin, cos, sqrt

# Parâmetros e condições iniciais

time_a = 0
time_b = 100 # s
g = 9.81 # ms^-1
l = 0.1 # m
C = 2 # s^-2
"""
#Letra (a) 
Omega = 5 # s^-1
"""
# Letra (b)
Omega = sqrt(g/l) # frequência natural do oscilador 


def f(r, t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta) + C*cos(theta)*sin(Omega*t)
    
    return array([ftheta, fomega], float)

def RK4(r, t):
    k1 = h*f(r, t)
    k2 = h*f(r+k1/2, t+h/2)
    k3 = h*f(r+k2/2, t+h/2)
    k4 = h*f(r+k3, t+h)
    
    return r + (1/6)*(k1+2*k2+2*k3+k4)

# Resolvendo EDO
h = 0.01
tpoints = arange(time_a, time_b, h)
thetapoints = []
omegapoints = []
r = array([0, 0], float)

for t in tpoints:
    thetapoints.append(r[0])
    omegapoints.append(r[1])
    r = RK4(r, t)


"""
# Letra A

pl.plot(tpoints, thetapoints, color='c', label='$\Omega = 5 s^{-1}$')
pl.legend()
pl.title('Theta em Função do Tempo')
pl.xlabel('$t$')
pl.ylabel('$\Theta(t) $')
pl.show()
pl.clf()
"""
# Letra B

pl.plot(tpoints, thetapoints, color='orange', label='$\Omega = \sqrt{\dfrac{g}{L}} \,\, s^{-1}$')
pl.legend()
pl.title('Theta em Função do Tempo')
pl.xlabel('$t$')
pl.ylabel('$\Theta(t) $')
pl.show()
