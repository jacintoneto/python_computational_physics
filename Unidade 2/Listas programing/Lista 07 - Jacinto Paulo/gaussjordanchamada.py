#from numpy.linalg import solve 
import numpy as np
from gaussjordan import gaussjordan

A = np.loadtxt('MatrixA.txt', float)
D  = np.copy(A)
v = np.loadtxt('VectorV.txt', float)
x = np.copy(v)

D, x = gaussjordan(D,x)

print("\n\nD:\n", D, "\n\nSolução[s]: \n", x)
