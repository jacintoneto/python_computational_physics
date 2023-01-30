"""
@author: Jacinto Paulo
"""
from numpy import zeros, array

def thomasjackalg(A, v):
    n = len(v)
    for m in range(n-1):
        i = m + 1
        #div = A[m,m]
        v[m] /= A[m, m]
        A[m, :] /= A[m, m] 
        
        #mult = A[i, m]
        v[i] -= A[i, m]*v[m]
        A[i,:] -= A[i, m]*A[m,:]

    
    v[-1] /= A[-1,-1]
    A[-1,-1] = 1.0
    #Substituição retrocedida
    # x = solução
    x = zeros(n, float)
    x[-1] = v[-1]

    for i in range(m-1,-1,-1):
        x[i] = v[i] - A[i,i+1]*x[i+1]
 
    return x
