"""
Desenvolvido por: Jacinto Paulo da Silva Neto
Disciplina: Física Computacional I
Prof.: Leonardo Dantas Machado

Lista 3 - Problema 2 Letra A e B - A constante de Stefan–Boltzmann
"""
import numpy as np
from math import exp
from gaussxw import gaussxwab
from scipy.constants import hbar, k, c

def f(z):
	return (((z/(1 - z))**3/(np.exp(z/(1 - z)) - 1))/(1 - z)**2)

def Gauss(N):
	a = -1 
	b = 1 
	x, w = gaussxwab(N, a, b)
	I = 0.0
	for i in range(N):
		I += w[i]*f(x[i])
	
	return I

#k - JK^-1
#hbar Js
#c ms^-1

N = 50

S = Gauss(N)
print("\n O valor da integral: ", S)

sigma = (k**4)/(4*np.pi**2*c**2*hbar**3)*S
print("\n A constante de Stefan-Boltzmann: ", sigma)

"""
(a) Eu fiz uma substituição de variavéis afim de contornar o limite de integração no infinito já que não conseguiria representar isso com muita veracidade. Posso afirmar que através desse método eu consigo um valor bem aceitável para integral. Eu fiz o teste com f(x) = x^4 - 2x +1, a = 0 e b = 2, o resultado foi 4.4! Mesmo considerando que a função polinomial é mais simples, (b) quando comparamos o valor da constante sigma obtido (σ = 5.67036681455e-08) com esse código com o da literatura (σ = 5.670367(13)×10−8 W⋅m−2⋅K−4), os valores são muito parecido no SI.
"""
