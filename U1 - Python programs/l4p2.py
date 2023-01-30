"""
Desenvolvido por: Jacinto Paulo da Silva Neto
Disciplina: Física Computacional I
Prof.: Leonardo Dantas Machado

Lista 4 - Problema 2 Letra A - Método polinomial de 3ª ordem
"""

from math import tanh
from pylab import *

def f (x): 
    return 1 + 1/2*tanh(2*x)

x = linspace(-2,2)

h = [0.1, 0.5, 1.0, 1.5] # Nas imagens se vê que não houve muita diferença comparada com o método diferenças centradas.


for i in h:
    dernumerica = ((1/24)*f(x + (-3/2)*i) - (27/24)*f(x - (1/2)*i) +(27/24)*f(x + (1/2)*i) - (1/24)*f(x + (3/2)*i))/i
    scatter(x, dernumerica, label = i)

title('Numérico vs Analítico')
legend()   

deranalitica = -tanh(2*x)**2 + 1
plot(x, deranalitica,label = 'analitica')
legend()
show()
