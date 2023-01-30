# Desenvolvido por: Jacinto Paulo da Silva Neto
# Problema 4: Integral Númerica - Regra de Simpson
print("\nEsse programa calcula a integral de  f(x)=x⁴-2x+1.\n")
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return (x**4 - 2*x + 1)

# REGRA DE SIMPSON
N = 10
a = 0
b = 2

while (N <= 1000):
	h =(b-a)/N
	parte_par = 0
	parte_impar = 0
	for k in range(1, N, 2):
		parte_impar += f(a + k*h)
	for k in range(2, N, 2):
		parte_par += f(a + k*h)
	I = (h/3)*(f(a) + f(b) + 4*parte_impar + 2*parte_par)
	erro = abs(I-4.4)*100/4.4
	print("\n\nA integral para N = ", N, " é: ", I)	
	print("\nErro relativo para N = ", N, " é: ", erro, "%")
	N = N*10

# a) Observei que com a regra do trapézio (4.50656) o resultado é superior ao resultado analítico (4.4), assim como através da regra de Simpson (4.400426666666667). Contudo, como podemos ver o resultado através da regra de Simpson é muito mais próximo e preciso.

# b) O erro relativo é dado por abs(I_N-4.4)*100/4.4; 

# c) O programa foi modificado (há uma foto disponível no rar com o código anterior). A diferenção em relação ao método do trapézio, é que nessa regra ao aumentar o número de fatias N a precisão aumenta ao invés de diminuir.
