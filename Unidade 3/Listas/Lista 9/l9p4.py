# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:37:48 2019

@author: Jacinto Paulo
Professor: Leonardo Machado
Disciplina: Física Computacional I
Lista 9 - Problema 4

"""
import pylab as pl
from numpy import array, arange, sin, pi

# Parâmetros e condições iniciais

time_a = 0
time_b = 5
g = 9.81 # ms^-1
l = 0.1 # m
N = 500
n = 3*pi/2 #Dessa maneira temos o pêndulo na vertical.

def f(r, t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    
    return array([ftheta, fomega], float)

def RK4(r, t):
    k1 = h*f(r, t)
    k2 = h*f(r+k1/2, t+h/2)
    k3 = h*f(r+k2/2, t+h/2)
    k4 = h*f(r+k3, t+h)
    
    return r + (1/6)*(k1+2*k2+2*k3+k4)

# Resolvendo EDO
h = (time_b - time_a)/N
tpoints = arange(time_a, time_b, h)
thetapoints = []
omegapoints = []
r = array([n - pi/2, 0], float)

for t in tpoints:
    thetapoints.append(r[0])
    omegapoints.append(r[0]*t)
    r = RK4(r, t)

pl.plot(tpoints, omegapoints, color='orange')
pl.title('Omega em Função do Tempo')
pl.xlabel('$t$')
pl.ylabel('$\omega(t) $')
pl.show()
pl.clf()
pl.plot(tpoints, thetapoints, color='c')
pl.title('Theta em Função do Tempo')
pl.xlabel('$t$')
pl.ylabel('$\Theta(t) $')
pl.show()