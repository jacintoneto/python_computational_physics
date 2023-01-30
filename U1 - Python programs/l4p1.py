"""
Desenvolvido por: Jacinto Paulo da Silva Neto
Disciplina: Física Computacional I
Prof.: Leonardo Dantas Machado

Lista 4 - Problema 1
"""

from math import tanh
from pylab import *

def f (x): 
	return 1 + 1/2*tanh(2*x)

h = [0.1, 0.5, 1.0, 1.5]
x = linspace(-2,2)

for i in h:
	dernumerica = (f(x + i/2) - f(x - i/2))/i
	scatter(x, dernumerica, label = i)

title('Numérico')
legend()
show()    

clf()

deranalitica = -tanh(2*x)**2 + 1
plot(x, deranalitica,label = 'analitica')
title('Analítico')
legend()
show()

# A medida que diminuimos o valor de h, a solução númerica fica mais próxima de do valor analítico.
