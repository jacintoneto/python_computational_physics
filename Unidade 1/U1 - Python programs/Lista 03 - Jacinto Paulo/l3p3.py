"""
Desenvolvido por: Jacinto Paulo da Silva Neto
Disciplina: Física Computacional I
Prof.: Leonardo Dantas Machado

Lista 3 - Problema 3 Letra B e C - Incerteza quântica no oscilador harmônico
"""
from gaussxw import *
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def f(z):
	x2 = (z/(1-z**2))**2
	fator = (1+z**2)/(1-z**2)**2
	
	return fator*x2*(abs(Psi(n, (z/(1-z**2)))))**2

def Gauss(N):
	a = -1
	b = 1
	y, w = gaussxwab(N, a, b)
	I = 0.0
	for k in range(N):
		I += w[k]*f(y[k])
	
	return I

def Hermite(n, x): 
    if (n == 0):
        return 1
    elif (n == 1):
        return 2*x
    else:
        return 2*x*Hermite(n-1,x) - 2*(n-1)*Hermite(n-2,x)

def Psi(n, x):
	const = (1/np.sqrt(2**n*factorial(n)*np.sqrt(np.pi)))
	return const*np.exp(- x**2/2)*Hermite(n,x)


n = [0,1,2,3]
x = np.linspace(-4, 4, 500)	

for i in n:
	plt.plot(x, Psi(i, x),label = i)

plt.legend()
plt.xlabel('x')
plt.ylabel('Psi(x)')
plt.show()

x = np.linspace(-10,10,500)
plt.plot(x, Psi(30, x))
plt.xlabel('x')
plt.ylabel('Psi(x)')
plt.show()

# incerteza

n = 5
N = 100

integ_x = Gauss(N)
incerteza_x = np.sqrt(integ_x)

print("\n Incerteza: ", incerteza_x)
