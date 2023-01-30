from numpy import empty

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

	



"""
# Backsubstitution
	x = empty(n, float)

	for m in range(n-1, -1, -1):
		x[m] = v[m]
		for i in range(m+1, n):
			x[m] = x[m] - A[m,i]*x[i]
	return x
"""
