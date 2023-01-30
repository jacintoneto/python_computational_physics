# Desenvolvido por: Jacinto Paulo da Silva Neto
# Problema 1: Equações quadráticas

from math import *
#a)
print("\nDado uma função quadrática do tipo f(x) = ax² + bx + c. Este algoritmo calcula as raízes dessa função.\n")

a = float(input("\nInforme o valor de a: "))
b = float(input("\nInforme o valor de b: "))
c = float(input("\nInforme o valor de c: "))

# Teste sugerido: 3x^2 - 4x + 1 = 0 ||| FEITO! Agradeço!
# Teste 2: 5x^2 + 4x - 1 = 0 ||| Está funcionando melhor! Certo!

delta = b**2 - 4*a*c
dif = b - sqrt(delta)
print("\nDelta = ", delta)
print("\nA diferença: b - raiz²[delta] = ", dif)

#a) primeiro método 
x_1 = (-b + sqrt(delta))/(2*a)
x_2 = (-b - sqrt(delta))/(2*a)

print("\n**PRIMEIRO MÉTODO**\nx_1 = ", x_1, "\nx_2 = ", x_2)

#b) segundo método --> "O que você encontrou? Como você explica isso?"
x_1 = (2*c)/(-b - sqrt(delta))
x_2 = (2*c)/(-b + sqrt(delta)) 

print("\n**SEGUNDO MÉTODO**\nx_1 = ", x_1, "\nx_2 = ", x_2)

# Percebi que onde há uma diferença geralmente irá produzir um resultado mais impressiso. Observei que o produto a*c tem muitos números após a vírgula, bem mais que b^2. Além disso, b² >> a*c. No momento de calular a (b - raiz²[delta]), haverá perda da precisão. Isso ocorre exatamente pelo mesmo motivo discutido no problema anterior associado a pontos flutuantes e operações de diferenças.


#c) terceiro método: afim de obter resultados mais preciso para as duas raízes, utilizarei apenas os resultados que não envolvem diferenças entre pontos flutuantes.

x_2 = (-b-sqrt(delta))/(2*a)
x_1 = (2*c)/(-b - sqrt(delta))

print("\n**TERCEIRO MÉTODO**\nx_1 = ", x_1, "\nx_2 = ", x_2)
 
