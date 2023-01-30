import numpy as np
from gaussjordan import gaussjordan
from time import monotonic

t1 = monotonic()
A = np.loadtxt('matriz3.txt', float); D = np.copy(A)
v = np.loadtxt('vetor3.txt', float); s = np.copy(v)

D,s = gaussjordan(D,s)
t2 = monotonic()

print("\n\nMatriz D:\n", D, "\n\nSolução: \n", s)
print ("\n\nO tempo gasto foi: ", t2-t1)
