# Exercício 2.1: Operações básicas

# Escreva um programa que pede ao usuário dois números, e em seguida fornece:

x = float(input("Informe o primeiro numero: "))
y = float(input("Informe o segundo numero: "))

# a) produto dos dois números
a = x*y

print("O produto entre", x," e ", y, " é: ", a)

# b) A parte inteira e o resto da divisão do primeiro pelo segundo

bi = x//y 
br = x%y

print("A parte inteira da divisão de", x,"por", y,"é: ", bi)
print("O resto da divisão de", x,"por", y,"é: ", br)

