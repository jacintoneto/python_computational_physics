#Exercício 2.6: Trabalhando com listas
from math import*

print("Utilize a função range() para gerar uma lista contendo todos os inteiros impares menores que 20. Em seguida, determine e imprima: \n\n")

r = list(range(1, 20, 2))
print(r)

print("a) A soma e o numero de elementos da lista.")
soma = sum(r)
num = 20/2
print("Soma: ", soma,";\nQntdd de elementos: ", num)

print("\n\nb) O maior e o menor elemento da lista.")
a = max(r)
b = min(r)
print("Maior: ",a, ";\nMenor: ", b)

print("\n\nc) O valor medio dos elementos da lista.")
medio = sum(r)/20/2
print("Valor médio: ", medio)

print("\n\nd) Uma lista contendo o logaritmo de cada membro da lista inicial.")
logaritmo = list(map(log, r))
print(logaritmo)


