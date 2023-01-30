"""
Desenvolvido por: Jacinto Paulo
Professor: Leonardo Machado
Disciplina: Física Computacional I
Lista 11 - Problema 1 - Órbitas de Cometas

Letra A e B 
"""
from numpy import array, arange, sqrt
import pylab as pl

# Constantes
M = 1.9891e30 # kg
G = 66374.2  # m^3.kg^-1*anos^-2
k = M*G
ti = 0; tf = 165 # anos
N = 1000000
h = (tf - ti)/N

tpoints = arange(ti, tf, h)
def f(r, t):
	x, y, vx, vy = r
	R = sqrt(x**2 + y**2)
	ax = -k*x/R**3
	ay = -k*y/R**3
	return array([vx, vy, ax, ay], float)

xpoints = [] 
ypoints = [] 
x0 = 4e12; y0 = 0 # m 
vx0 = 0; vy0 = 15768000000 # m.ano^-1
r = array([x0, y0, vx0, vy0], float) # x = r[0], y = r[1], vx = r[2], vy = r[3]

for t in tpoints:
	xpoints.append(r[0])
	ypoints.append(r[1])
	k1 = h*f(r, t)
	k2 = h*f(r+k1/2, t+h/2)
	k3 = h*f(r+k2/2, t+h/2)
	k4 = h*f(r+k3, t+h)
	r += (k1+2*k2+2*k3+k4)/6

x = array(xpoints, float); y = array(ypoints, float)

pl.plot(x, y,'.', color='c')
pl.legend()
pl.xlabel('$x(km)$')
pl.ylabel('$y(km)$')
pl.title('Órbitas de Cometas - Método RK4')
pl.show()

"""
A) dx/dt = f(x,t) .: df/dt = -kx/r³
   dy/dt = g(y,t) .: dg/dt = -ky/r³

B)
Observei que se eu utilizar um tempo muito pequeno como nos exercícios anteriores eu irei obter um reta vertical. É necessário utilizar um tempo maior nesse caso, em anos. O programa demorou uma quantidade aceitável de tempo, cerca de 8 segundos para fazer o plot.
"""
