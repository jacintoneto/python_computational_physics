# Desenvolvido por: Jacinto Paulo da S. Neto
# Lista 2 - Problema 2

import matplotlib.pyplot as plt
import numpy as np
from math import *

# a)
def f(m, teta, x):
	return cos((m*teta) - (x*sin(teta)))

def simpson(m, x): # J --> simpson --> f
#	a = 0; b = pi
	h = np.pi/1000
	p_par = 0
	p_impar = 0
	for k in range(1, 1000, 2):
		p_impar += f(m, k*h, x)
	for k in range(2, 1000, 2):
		p_par += f(m, k*h, x)
	return (h/3)*(f(m, 0, x) + f(m, pi, x) + 4*p_impar + 2*p_par)

def J(m, x):	
	return (1/pi)*(simpson(m, x))	

# N = (input("Informe a quantidade de fatias: ")) ; N = 1000
x = np.linspace(0, 20, 1000)

J_0 = np.empty(1000, float)
J_1 = np.empty(1000, float)
J_2 = np.empty(1000, float)

for i in range(0, 1000):
	J_0[i] = J(0, x[i])
	J_1[i] = J(1, x[i]) 
	J_2[i] = J(2, x[i])

plt.plot(x, J_0, label = "J0(x)")
plt.plot(x, J_1, label = "J1(x)")
plt.plot(x, J_2, label = "J2(x)")
plt.title("Função de Bessel")
plt.xlabel("x")
plt.ylabel("Jn(x)")
plt.show()

# b) Gráfico de Intensidade

M = np.zeros([100,100], float)
K = (2*pi)/5e-7
for i in range(0, 100):
	for j in range(0, 100):
		r = sqrt((i - (100/2))**2 + (j - (100/2))**2)*1e-8 # r = 1.0e-6
		if (K*r < 10**(-6)):
			M[i,j] = 0.5 
		else:
			M[i,j] = (J(1, K*r)/(K*r))**2

plt.imshow(M, vmax = 0.01, cmap = "hot")
plt.title("Padrão de Difração Circular")
plt.show()



