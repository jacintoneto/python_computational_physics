# Desenvolvido por: Jacinto Paulo da S. Neto
# Lista 2 - Problema 1

import numpy as np
from math import *
import matplotlib.pyplot as plt

def f(t):
	return np.exp(-t**2)


def trapezio(a, b, N): # b = x = i, a = 0;
	h = (b-a)/N
	soma = 0.5*(f(b) + f(a))
	for k in range(1, N):
		soma += f(a + k*h)
	return h*soma


def E(x):
	return trapezio(0, x, 100) #N=100

x = 3; a = 0; I = 0; i=0; c=0
v = np.empty(30,float) # tamanho = x/0.1 = 30
fun = np.empty(30,float)
while(i <= x):
	I += E(i) 
	i += 0.1
	print("\n ------ ---- ---- \n\nx = ", i, "\nE(x) = ", I)	
	v = np.append(v, i)	
	fun = np.append(fun, I)

plt.plot(v, fun)
plt.xlabel("x")
plt.ylabel("E(x)")
plt.show()






