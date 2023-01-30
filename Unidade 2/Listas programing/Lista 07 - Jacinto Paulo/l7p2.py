"""
Aluno: Jacinto Paulo da Silva Neto
Disciplina: Física Computacional I
Prof.: Leonardo Dantas Machado

Lista 7 - Problema 2 - Pivotamento
"""

from numpy.linalg import solve 
from numpy import array, empty, loadtxt
from gausseli import gausseli

A = loadtxt('MatrixB.txt', float)
u = loadtxt('VectorU.txt', float)
N = len(u)

# Variáveis auxiliares
a = empty(N, float)
b = empty(N, float)


#Solve's solution
v = solve(A,u)
print("Solve's solution: ", v, "\n\n")

# Newman-Jacinto solution 
w = empty(N, float)

print(A, "\n\n", u,"\n\n")

# Pivotamento
if(A[0,0] == 0):
	for m in range(N):
		if(abs(A[0,0]) < abs(A[m,0])):
			for i in range(N):
				a[i] = A[0, i]
				A[0,i] = A[m,i]
				A[m,i] = a[i]
			b[m] = u[0]	
			u[0] = u[m]
			u[m] = b[m]			 

print(A,"\n\n", u,"\n\n")

w = gausseli(A, u)
print("Newman-Jacinto solution: ", w)

