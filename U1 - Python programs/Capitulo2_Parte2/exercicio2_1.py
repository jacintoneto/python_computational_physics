# Exercício 2.1: Trabalhando com o “for”.

print("Este algoritmo usa a função range num for para gerar sequência de números!\n\n")
print("Para que o programa seja o mais geral possível, você deverá inserir três parâmetros requisitados.\n\n")
print("**DICA**\nPara gerar uma sequência em ordem decrescente inicie com o maior número,\ntermine com o menor e coloque o passo negativo!!!")
print("\nn = teto da sequência;\ni = inicio da sequência; e\np = passo.\n\n")

i = int(input("Informe i: "))
n = int(input("Informe n: "))
p = int(input("Informe p: "))

print("\n\nOs números gerados são: ")

for j in range(i, n, p):
	print(j)
