#from numpy.linalg import solve 
import numpy as np

def gausseli(A, v):
	n = len(v)
	for m in range(n):
	
	# Divide by the diagonal element
		div = A[m,m]
		A[m,:] = A[m,:]/div
		v[m] = v[m]/div

	# Now subtract from lower row7s
		for i in range(m+1, n):
			mult = A[i,m]
			A[i,:] = A[i,:] - mult*A[m,:]
			v[i] = v[i] - mult*v[m]

# Backsubstitution
	x = np.empty(n, float)

	for m in range(n-1, -1, -1):
		x[m] = v[m]
		for i in range(m+1, n):
			x[m] = x[m] - A[m,i]*x[i]
	return A, x, v

def f(U, v):
	n = v.size
	for j in range(n-1):
		for k in range(j+1, n):
			mult = U[j,k]
			U[j,:] += -mult*U[k,:]
			v[j] += -mult*v[k]
	
	return U, v

A = np.loadtxt('MatrixA.txt', float)
U = np.copy(A)
v = np.loadtxt('VectorV.txt', float)
x = np.copy(v)
va = np.empty(x.size, float) #v alterado

U, x, va = gausseli(U,x)

D = np.copy(U)
s = np.copy(va)

D, s = f(D,s) 

print("A:\n",A, "\n\nU: \n", U,"\n\nSolução[x]:\n", x, "\n\nD:\n", D, "\n\nSolução[s]: \n", s)
