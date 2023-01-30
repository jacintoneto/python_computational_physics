# teste fatiamento

from numpy import*

A = loadtxt("matrixA.txt",int)
print("A matriz A: \n", A)

# fatiamento

#linha0 = A[0,:]; linha1=A[1,:]; linha2=A[2,:] 
#coluna0 = A[:,0]; coluna1=A[:,1]; coluna2=A[:,2]
#print("\n\nColuna 1: ", coluna0) gera => [1 4 7]
#print("\n\nColuna 2: ", coluna1) gera => [2 5 8]
#print("\n\nColuna 3: ", coluna2) gera => [3 6 9]

for i in range(0,3,1):
	linha = A[i,:]
	


