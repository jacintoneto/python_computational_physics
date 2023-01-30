#Exerc´ıcio 2.7: Copiando vetores

print("\n-----------------------JACKSTARDUST---------------------------")
print("\nEste algoritmo faz copias de maneiras distintas.\n")

from numpy import *
print("---- *1ª maneira de passagem de cópia ------------")
a = [1,1]
print("\n\nA vetor a: \n",a)
b = a
print("\n\nA vetor b: \n", b)

print("\nAlterando o valor em a...\n")
a[0] = 2

print("\nA vetor a: \n",a)
print("\n\nA vetor b: \n", b)

print("\n\n ---- *2ª maneira de passagem de cópia ------")
a = [1,1]
print("\n\nA vetor a: \n",a)

b = copy(a)
print("\nA vetor b: \n", b)

print("\nAlterando o valor em a...\n")
a[0]=2

print("\nA vetor a: \n",a)
print("\n\nA vetor b: \n", b)
