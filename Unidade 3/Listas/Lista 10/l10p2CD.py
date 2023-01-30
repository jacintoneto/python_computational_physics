# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 14:17:14 2019

@author: Jacinto Paulo
Professor: Leonardo Machado
Disciplina: Física Computacional I
Lista 10 - Problema 2 - Letras C e D - Oscilador anarmônico 

"""
import pylab as pl
from numpy import array, arange

# Parâmetros e condições iniciais
time_a = 0
time_b = 50
w = 1

def f(r, t):
    x = r[0]
    y = r[1]
    fx = y
    fy = -w**2*x**3
    
    return array([fx, fy], float)

def RK4(r, t):
    k1 = h*f(r, t)
    k2 = h*f(r+k1/2, t+h/2)
    k3 = h*f(r+k2/2, t+h/2)
    k4 = h*f(r+k3, t+h)
    
    return r + (1/6)*(k1+2*k2+2*k3+k4)

def solve(r, t):
    xpoints = []
    ypoints = []
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        r = RK4(r, t)
    
    return xpoints, ypoints
    
# Resolvendo EDO
h = 0.01
tpoints = arange(time_a, time_b, h)

r = array([1, 0], float)
xpoints, ypoints = solve(r, tpoints)

pl.plot(tpoints, xpoints, color = 'red', label='x = 1')
pl.legend()
pl.title('Oscilador Anarmônico')
pl.xlabel('$t$')
pl.ylabel('$x(t)$')
pl.show()
pl.clf()



pl.plot(xpoints, ypoints, color= 'red', label='x=1')
pl.legend()
pl.title("Espaço de Fase do Oscilador Anarmônico")
pl.xlabel('$x(t)$')
pl.ylabel('$y(t)$')
pl.show()
pl.clf()

r2 = array([2, 0], float)
xpoints2, ypoints2 = solve(r2, tpoints)

pl.plot(tpoints, xpoints2, label='x = 2')
pl.legend()
pl.title('Oscilador Anarmônico')
pl.xlabel('$t$')
pl.ylabel('$x(t)$')
pl.show()
pl.clf()

# Espaço de Fase Anarmônico

pl.plot(xpoints2, ypoints2, label='x = 2')
pl.legend()
pl.title("Espaço de Fase do Oscilador Anarmônico")
pl.xlabel('$x(t)$')
pl.ylabel('$y(t)$')
pl.show()
pl.clf()