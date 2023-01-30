import numpy as np
from gausseli import gausseli
from time import monotonic

t1 = monotonic()
A = np.loadtxt('matriz3.txt', float); U = np.copy(A)
v = np.loadtxt('vetor3.txt', float); x = np.copy(v)

U,x = gausseli(U,x)
t2 = monotonic()

print("\n\nMatriz U:\n", U, "\n\nSolução x: \n", x)
print ("\n\nO tempo gasto foi: ", t2-t1)
