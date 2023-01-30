# Desenvolvido por: Jacinto Paulo da S. Neto
# Lista 2 - Problema 2

import matplotlib.pyplot as plt
import numpy as np
from math import *

# a) J(m,x)
# Note: os limites são fixos.


def simpson(m, x, a, b, N): # J --> simpson --> f
	h = (b-a)/N
	p_par = 0
	p_impar = 0
	for k in range(1, N, 2):
		p_impar += f(m, x, a + k*h)
	for k in range(2, N, 2):
		p_par += f(m, x, a + k*h)
	return (h/3)*(f(m, x, a) + f(m, x, b) + 4*p_impar + 2*p_par)

def f(m, x, teta):
	return (np.cos(m*teta - x*np.sin(teta)))

def J(m, x, N):
	a = 0; b = pi
	return (1/pi)*(simpson(m, x, a, b, N))			

N = 1000
B = np.linspace(0, 20, 100)
y = np.linspace(0, 20, 100)

for i in range(0, 4): # i = m
	for k in range(0, 21): # k = x
		B[k] = J(i, k, N)
		y[k] = k
print(B)
plt.plot(y, B)
plt.show()
