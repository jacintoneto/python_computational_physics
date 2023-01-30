"""
Aluno: Jacinto Paulo da Silva Neto
Disciplina: Física Computacional I
Prof.: Leonardo Dantas Machado

Lista 7 - Problema 1 Letra B, C.
"""

from numpy import array, empty, loadtxt
from numpy.linalg import solve 

A = loadtxt('MatrixA.txt', float)
v = loadtxt('VectorV.txt', float)

N = len(v)

# b)
# Gaussian elimination
for m in range(N):
	
	# Divide by the diagonal element
	div = A[m,m]
	A[m,:] = A[m,:]/div
	v[m] = v[m]/div
	#print("\n", A, "\n\n", v)


	# Now subtract from lower row7s
	for i in range(m+1, N):
		mult = A[i,m]
		A[i,:] = A[i,:] - mult*A[m,:]
		v[i] = v[i] - mult*v[m]
	#print("\n", A, "\n\n", v)

# Backsubstitution
x = empty(N, float)

for m in range(N-1, -1, -1):
	x[m] = v[m]
	for i in range(m+1, N):
		x[m] = x[m] - A[m,i]*x[i]

print("Solução: \n", x)

# c)
y = empty(N, float)
solve(A, y)

print("\n\nSolve: \n", y)

