# Exercício 2.2: Soma dos inversos

print("Este programa calcula a somatória de 1/k.\n\n")

n = int(input("Informe até qual valor de n você deseja somar 1/k: "))
s = 0
for k in range(1,n,1):
	s = s + 1/k
print("\n\nA soma total é: ", s)
