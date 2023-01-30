# teste 3
from numpy import *

a = loadtxt("matrixA.txt", int)
print(a)

maior = 0

for i in range(0,3,1):
	for j in range(0,3,1):
		aux = a[i,j]
		if(maior<aux):
			maior = aux
			l = i; c = j

print("\n\nO maior valor é ", maior, " e está na posição ", l, "x", c,".")


