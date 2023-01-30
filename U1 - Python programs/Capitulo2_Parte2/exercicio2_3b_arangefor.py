# Exercício 2.3: Criando vetores e matrizes
# b) A matriz A (dada no pdf). Tente realizar este procedimento tres vezes, usando as funções zeros, array e loadtxt.

# 1/ FUNÇÃO ZEROS 
from numpy import *

A = zeros([3,3], int)
k = 1
for i in range(0,3,1):
	for j in range(0,3,1):	
		A[i,j] = k
		k = k + 1
print(A)	

