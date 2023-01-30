# Desenvolvido por: Jacinto Paulo da S. Neto
# Lista 2 - Problema 4 

# b) Método de Romberg  

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

def R(i, m):
	if (m == 1): # não se calcula erro aqui
		N = 2**(i-1)
		return trapezio(a, b, N)
	else:
			 # m --> m - 1; m + 1 --> m; i permaneceu.

		return RM[i, m-1] + (RM[i, m-1] - RM[i-1, m-1])/(4**(m-1) - 1)

a = 0; b = 2; N = 1; erro = 1000; i = 1; lim = 1.0e-6
#p = int(input("Informe o número de colunas: "))
p =10
RM = np.zeros([p,p], float)
RM[1,1] = R(1,1)
i+=1
#print(RM[1,1])
while(erro > lim):
	for m in range(1, i+1): #printing linha i = fixo, correndo coluna.
		RM[i,m] = R(i,m)
		print(RM[i,m], end='  ')
	erro = abs((1/4**(i-1) - 1)*(RM[i, i-1] - RM[i-1,i-1]))
	i+=1
	print()

print("\n", 2**(i-2)," ", RM[i-1, m], " ", erro)

"""
RM[1,1] = trapezio(a,b,N) #I1
RM[2,1] = 
print(RM[1,1])

for i in range(0, p):
	RM[i, 0] = trapezio(a, b, N)
	N = 2**i
	print(RM[i,0])
"""

		
