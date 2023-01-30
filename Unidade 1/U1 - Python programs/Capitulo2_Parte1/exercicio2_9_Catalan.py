# Exercício2_9 - Série de Catalan
# Escreva um programa que imprima em ordem crescente todos os numeros de Catalan menores que um bilhão.
# C_0 = 1; C_(n+1) = (4n-2/n+1)C_n ; n=>0.

teto = int(input("\nInforme um valor teto para os números de Catalan: "))
C = 1
n = 1

if(teto <= 1):
	print(C)
else:
	print(C)
	while(C <= teto):
		print(C)
		C = ((4*n+2)/(n+2))*C
		n = n + 1


