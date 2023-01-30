"""
Desenvolvido por: Jacinto Paulo da Silva Neto
Disciplina: Física Computacional I
Prof.: Leonardo Dantas Machado

Lista 4 - Problema 2 Letra C - Método da 3ª Ordem e Cálculo de Erros - l4p2C.py
"""
from numpy import *
from math import tanh
from pylab import *

def f (x): 
    return 1 + 1/2*tanh(2*x)

x = 0.0
h = [0.01, 0.001, 1.0e-4, 1.0e-5, 1.0e-6, 1.0e-7] 
deffanalitica = -tanh(2*x)**2 + 1
aux = 10e10
print("\n Derivada analítica: ", deffanalitica, "\n")
print("	   h 	 	 |	DerivadaNumérica	| 	Erro \n")
for i in h:
	deffnumerica = ((1/24)*f((-3/2)*i) - (27/24)*f((1/2)*i) + (27/24)*f((1/2)*i) - (1/24)*f((3/2)*i))/i
	erro = abs(deffnumerica - deffanalitica)
	if (erro < aux):
		minimiza = i

	print("	", i, "  	 | 	  ", deffnumerica, "  	|   ", erro)
	aux = erro

print("\n O valor de h que minimiza o erro é: ", minimiza)

"""
Os valores obtidos através desse método são péssimos, o erro é muito alto comparado ao método anterior, das diferenças centrais. Isso acontece pois a derivada é constante = 1, o termo variável em x morre, e então utilizar um polinômio de ordem 3 não ajuda, mas sim atrapalha. 
"""
