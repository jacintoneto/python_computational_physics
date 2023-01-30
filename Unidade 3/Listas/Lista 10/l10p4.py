"""
Desenvolvido por: Jacinto Paulo
Professor: Leonardo Machado
Disciplina: Física Computacional I
Lista 10 - Problema 4 - Lixos Espaciais
"""

from numpy import array, arange, sqrt
import pylab as pl

# Constantes do sistema
G = 1
M = 10
k = G*M
L = 2

time_a = 0
time_b = 10
h = 0.01
tpoints = arange(time_a, time_b, h)

def f(r, t):
	x = r[0]
	fx = r[1]
	y = r[2]
	fy = r[3]
	r = sqrt(x**2 + y**2)
	ffx = -(k*x)/r**2*sqrt(r**2 + L**2/4)
	ffy = -(k*y)/r**2*sqrt(r**2 + L**2/4)
	
	return array([fx, ffx, fy, ffy], float)

xpoints = []
ypoints = []
r = array([1, 0, 0, 1], float)

# buscando soluções das equações
for t in tpoints:
	xpoints.append(r[0])
	ypoints.append(r[2])
	k1 = h*f(r, t)
	k2 = h*f(r+k1/2, t+h/2)
	k3 = h*f(r+k2/2, t+h/2)
	k4 = h*f(r+k3, t+h)
	r += (k1+2*k2+2*k3+k4)/6

x = array(xpoints, float); y = array(ypoints, float)

pl.plot(x, y, color='orange')
pl.title('Órbita em Lixos Espaciais')
pl.legend()
pl.xlabel('$x$')
pl.ylabel('$y$')
pl.show()
