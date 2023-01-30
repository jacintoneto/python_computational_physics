#Exerc´ıcio 2.8:

print("\n-----------------------------JACKSTARDUST-------------------------------")
print("\nEste algoritmo usa fatiamento numa Matriz.\n")
from numpy import *

D = loadtxt("matrixD.txt", int)
print("Esta é a matriz D: \n", D)

#a)Um vetor cujos elementos sao os da primeira linha de D
print("\n\nElementos da primeira linha de D:\n")
l0 = D[0,:]
print(l0)

#b)Um vetor cujos elementos sao os da segunda coluna de D
print("\n\nElementos da segunda coluna de D:\n")
c1 = D[:,1]
print(c1)

#c) Um vetor contendo os dois ultimos elementos da terceira linha de D
print("\n\nOs dois ultimos elementos da terceira linha de D:\n")
l2_12 = D[2,1:]
print(l2_12)
