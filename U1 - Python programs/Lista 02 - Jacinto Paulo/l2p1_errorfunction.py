# Desenvolvido por: Jacinto Paulo da S. Neto
# Lista 2 - Problema 1 - Função Erro

import matplotlib.pyplot as plt
import numpy as np
from math import *

def f(t):
	return np.exp(-t**2)

def simpson(a, b, N): # E --> simpson --> f
	h = (b-a)/N
	p_par = 0
	p_impar = 0
	for k in range(1, N, 2):
		p_impar += f(a + k*h)
	for k in range(2, N, 2):
		p_par += f(a + k*h)
	return (h/3)*(f(a) + f(b) + 4*p_impar + 2*p_par)

def E(a, x, N):
	return simpson(a, x, N)

a = 0; b = 3; N = 30

# a) h = 0.1, N = 30. Isto é, a = 0 e b = 3.
print("O valor de E(x) = ", E(a, b, N))

# b) plot dos valores de E(x) versus x.
x = np.linspace(a,b,1000)
FE = np.empty(np.size(x),float)

for i in range(0, np.size(x)):
	FE[i] = E(a, x[i], N)

plt.plot(x, FE)
plt.xlabel("x")
plt.ylabel("E(x)")
plt.show()

