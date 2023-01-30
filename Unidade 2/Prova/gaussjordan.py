from numpy import *

def gaussjordan(A, v): 
# Gauss elimination - made by Newman.
	n = v.size
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

# Jordan diagonalization - made by me, Jacinto Paulo.
	#x = np.copy(v) # v alterado
	for j in range(n-1):
		for k in range(j+1, n):
			mult = A[j,k]
			A[j,:] += -mult*A[k,:]
			v[j] += -mult*v[k]
	
	return A, v
