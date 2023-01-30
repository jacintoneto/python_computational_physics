#Exercıcio 2.10: Mapeando funcoes definidas pelo usuário

#Crie o vetor a= [2,3,4,5]. Em seguida, crie um vetor b em que cada elemento é o fatorial de um elemento de a. 
#(Dica: Use a funcao “map” em conjunto com a funcao “fatorial” definida no exercıcio anterior para realizar esta tarefa em uma linha.)

print("\nEste algoritmo usa as funções map e fatorial em conjunto.\n\n")

from math import *
from numpy import *

def fatorial(n):
	f=1
	if (n==1):
		return 1
	else:
		for i in range(1,n+1,1):
			f = f*i
		return f

a = [2, 3, 4, 5]
print("O vetor a: \n", a)

b = list(map(fatorial, a))

print("\n\nO vetor b: \n", b)
