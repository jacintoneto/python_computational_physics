import numpy as np
from gaussjordan import gaussjordan

A = np.loadtxt('matrix.txt', float); D  = np.copy(A)
v = np.loadtxt('vetor.txt', float); s = np.copy(v)

D, s = gaussjordan(D,s)

print("\n\nMatriz D:\n", D, "\n\nSolução: \n", s)
