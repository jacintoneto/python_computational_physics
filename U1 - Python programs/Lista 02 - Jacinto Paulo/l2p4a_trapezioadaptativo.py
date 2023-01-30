# Desenvolvido por: Jacinto Paulo da S. Neto
# Lista 2 - Problema 4 

# a) Trapézio Adaptativo

import numpy as np
from math import *

def f(x):
	return (np.sin(np.sqrt(100*x)))**2

def trapezio(a, b, N):
	h = (b-a)/N
	soma = (f(a)+f(b))*0.5
	for k in range(1, N):
		soma += f(a + k*h)
	return h*soma

def adaptative(a, b, N, I_old):
	h = (b-a)/N
	soma = 0
	for k in range(1, N, 2):
		soma += f(a + k*h)
	I_new = 0.5*I_old + h*soma
	erro = abs((I_new - I_old))/3
	return I_new, erro

a = 0; b = 1; N = 1; erro = 1000; i = 0; lim = 1.0e-6

print("\n|	N		|		I   		 |	 Erro\n")
while(erro > lim):	
	if (i == 0):
		I_old = trapezio(a, b, N)
	else:
		I_new, erro = adaptative(a, b, N, I_old)
		I_old = I_new
	print("|	", N, "		|	 ", I_old, "	 | ", erro)
	N=2*N
	i+=1





