# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:01:17 2019

@author: Jacinto Paulo
Professor: Leonardo Machado
Disciplina: Física Computacional I
Lista 10 - Problema 2 - Letra E - Oscilador de Van der Pol

"""
import pylab as pl
from numpy import array, arange

# Parâmetros e condições iniciais
time_a = 0
time_b = 20
w = 1

def f(r, t, mu):
    x = r[0]
    y = r[1]
    fx = y
    fy = mu*(1-x**2)*y - w**2*x
    
    return array([fx, fy], float)

def RK4(r, t,mu):
    k1 = h*f(r, t, mu)
    k2 = h*f(r+k1/2, t+h/2, mu)
    k3 = h*f(r+k2/2, t+h/2, mu)
    k4 = h*f(r+k3, t+h, mu)
    
    return r + (1/6)*(k1+2*k2+2*k3+k4)

def solve(r, t, mu):
    xpoints = []
    ypoints = []
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        r = RK4(r, t, mu)
    
    return xpoints, ypoints
    
# Resolvendo EDO
h = 0.01
tpoints = arange(time_a, time_b, h)

r = array([1, 0], float)
mu = 1
xpoints, ypoints = solve(r, tpoints, mu)

pl.plot(xpoints, ypoints, color = 'c', label='mu = 1') #mu = 2, mu = 4
pl.legend()
pl.title('Oscilador de Van der Pol')
pl.xlabel('$x(t)$')
pl.ylabel('$y(t)$')
pl.show()
pl.clf()

mu = 2
xpoints, ypoints = solve(r, tpoints, mu)

pl.plot(xpoints, ypoints, color = 'orange', label='mu = 2') #mu = 2, mu = 4
pl.legend()
pl.title('Oscilador de Van der Pol')
pl.xlabel('$x(t)$')
pl.ylabel('$y(t)$')
pl.show()
pl.clf()

mu = 4
xpoints, ypoints = solve(r, tpoints, mu)

pl.plot(xpoints, ypoints, color = 'red', label='mu = 4') #mu = 2, mu = 4
pl.legend()
pl.title('Oscilador de Van der Pol')
pl.xlabel('$x(t)$')
pl.ylabel('$y(t)$')
pl.show()
pl.clf()