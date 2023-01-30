# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:17:11 2019

@author: Jacinto Paulo
Professor: Leonardo Machado
Disciplina: Física Computacional I
Lista 10 - Problema 3 - Trajetórias com Resistência do Ar
"""

from numpy import array, arange, pi, sin, cos, sqrt
import pylab as pl

# Constantes do sistema
#m = 1  # kg
g = 9.81 # m.s^-2
R = 0.08  # m
theta0 = 30*pi/180  # rad
v0 = 100  # m.s^-1
rho = 1.22  # kg.m^3
C = 0.47  # arrasto
k = pi*R**2*rho*C/2

time_a = 0
time_b = 6.7
h = 0.01
tpoints = arange(time_a, time_b, h)

def cte(m):
    return k/m

def f(r, t, m):
    x = r[0]
    fx = r[1]
    y = r[2]
    fy = r[3]
    v = sqrt(fx**2 + fy**2)
    ffx = -cte(m)*fx*v
    ffy = -g-cte(m)*fy*v
    return array([fx, ffx, fy, ffy], float)

# buscando soluções das equações
def solving(m):
    xpoints = []
    ypoints = []
    r = array([0, v0*cos(theta0), 0, v0*sin(theta0)], float)
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[2])
        k1 = h*f(r, t, m)
        k2 = h*f(r+k1/2, t+h/2, m)
        k3 = h*f(r+k2/2, t+h/2, m)
        k4 = h*f(r+k3, t+h, m)
        r += (k1+2*k2+2*k3+k4)/6
    x = array(xpoints, float); y = array(ypoints, float)
    return x, y

x, y = solving(1)
x2, y2 = solving(2)
x3, y3 = solving(3)
pl.plot(x, y, color='c', label='m = 1 kg')
pl.plot(x2, y2, color='orange', label='m = 2 kg')
pl.plot(x3, y3, color='black', label='m = 3 kg')
pl.title('Trajetórias com Resistência do Ar')
pl.legend()
pl.xlabel('$x$ (metros)')
pl.ylabel('$y$ (metros)')
pl.show()

"""
Podemos perceber que quão maior a massa da partícula mais longe ela consegue ir, i.é. maior será o alcanse. Enquanto que uma partícula mais leve rapadimente é forçada a encontrar o chão, passa menos tempo viajando no ar.
"""
