"""
Desenvolvido por: Jacinto Paulo da Silva Neto
Disciplina: Física Computacional I
Prof.: Leonardo Dantas Machado

Lista 3 - Problema 1 Letra B - Calor Específico de um Sólido
"""
import matplotlib.pyplot as plt
from math import *
import numpy as np
from gaussxw import gaussxw

def f(x):
	return x**4*exp(x)/(exp(x)-1)**2

def gauss(N):
	
	return I

def Cv(T):
	a = 0
	b = tetaD/T
	xp = 0.5*(b-a)*x + 0.5*(b+a)
	wp = 0.5*(b-a)*w
	I = 0.0

	for i in range(N):
		I+= wp[i]*f(xp[i])

	const = 9*V*rho*kB*(T/tetaD)**3

	return const*I


rho =6.022e28	# m^-3
V = 1e-3	# m^3
kB = 1.38e-23   # JK^-1
# T = float(input("\n>> Informe a temperatura do material: "))
tetaD =	428 	# K 
N = 100

x, w = gaussxw(N)

T = np.linspace(5, 500, N)
Calor = np.empty(N, float)  # Calor = [Cv(Ti) for Ti in T]

for i in range(1, N):
	Calor[i] = Cv(T[i])

plt.plot(T, Calor)
plt.xlabel('Temperature (K)')
plt.ylabel('Cv')
plt.show()


