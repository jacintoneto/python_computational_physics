# Desenvolvido por: Jacinto Paulo da S. Neto
# Lista 2 - Problema 3

import numpy as np
from math import *

def f(x):
	return x**4 - 2*x + 1

def trapezio(N): # a=0, b=2
	h = (2)/N
	I = 0.5*(f(2) + f(0))
	for k in range(1, N):
		I += f(k*h)
	return h*I

# calculando I1 e I2
N1 = 10
N2 = 20
I1 = trapezio(N1)
I2 = trapezio(N2)

print(I1, I2)
E = abs(I1 - I2)/3

print(E) # E = 0.026633333333333137 || 4.4 - I2 = 0.026660000000000572

# Apesar de serem valores próximo, sendo portanto semelhantes até o 4º algarismo significativo, devemos lembrar que estamos tomando o erro até 2ª ordem. 




