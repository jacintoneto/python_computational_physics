# Exercício 2.3: Criando vetores e matrizes
# b) A matriz A (dada no pdf). Tente realizar este procedimento tres vezes, usando as funções zeros, array e loadtxt.

# 1/ FUNÇÃO LOADTXT

from numpy import *

A = loadtxt("matrixA.txt", int)
print(A)
