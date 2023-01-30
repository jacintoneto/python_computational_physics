# Exercício 2.6: Operação com matrizes - parte 2
print("\n-----------------------------JACKSTARDUST-------------------------------")
print("\n\nEste algortimo faz operações com matrizes: maior, menor, media e raiz quadrada do numpy")

from numpy import *


B = loadtxt("matrixB.txt", int)
print("A matrix:\n", B)
print("--------------- letra a --------------")
# a) maior e menor elemento de B.
maior = 0
for i in range(0,3,1):
	for j in range(0,3,1):
		aux = B[i,j]
		if(maior<aux):
			maior = aux
			l = i; c = j

print("\nO maior valor é ", maior, " e está na posição ", l, "x", c,".")

menor = B.min()
print("\n\nO menor valor é: ", menor,"\n\n")

#b) O valor medio dos elementos da matriz B
print("--------------- letra b --------------")
soma = sum(B)
print("A soma dos elementos de B: ", soma)
print("A quantidade de elemento é: ", size(B))
medio = soma/size(B)
print("Então, o valor médio dos elementos de B é: ", medio)

#c) Para criar uma matriz C, em que cada elemento e a raiz quadrada de um elemento da matriz B.

C = sqrt(B)
print("\n\nA matriz C, que é a 'raiz quadrada' de B: \n", C)
