"""
Desenvolvido por: Jacinto Paulo da Silva Neto
Disciplina: Física Computacional I
Prof.: Leonardo Dantas Machado

Lista 4 - Problema 2 Letra B - Método da Diferença Centrada e Cálculo de Erros
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
	deffnumerica = (f(i/2) - f(-i/2))/i
	erro = abs(deffnumerica - deffanalitica)
	if (erro < aux):
		minimiza = i

	print("	", i, "  	 | 	  ", deffnumerica, "  	|   ", erro)
	aux = erro

print("\n O valor de h que minimiza o erro é: ", minimiza)
