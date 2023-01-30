# Exercício 2.5: operações com matrizes parte 1

# criando matriz B

from numpy import *

B = loadtxt("matrixB.txt", int)
print("A matriz B: \n", B)

# multiplicando por uma escalar
n = float(input("\n\nInforme o escalar que você deseja multiplicar por B: "))
C = n*B
print("\n\nA matriz C = n*B: \n", C, "\n\n")

#percebemos que tanto faz usar o dot(n, B) ou n*B, quando n é escalar.

#somando por outra matriz
A = loadtxt("matrixA.txt", int)
print("A matriz A: \n", A, "\n\n")

D = A+B
print("A matriz D = A+B: \n", D)

#multiplicando sem dot()
E = A*B
print("\n\nA matrix E = A*B: \n", E)

#multiplicando usando dot()
F = dot(A,B)
print("\n\nA matrix F=dot(A,B): \n", F)




