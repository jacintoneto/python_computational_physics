"""
Desenvolvido por: Jacinto Paulo da Silva Neto
Disciplina: Física Computacional I
Prof.: Leonardo Dantas Machado

Lista 4 - Problema 3 - 
"""

from math import *
from pylab import *


def f(x):
    return 1 + 1/2*tanh(2*x)

x = linspace(-2,2)
h = [1e-6, 1e-7, 1e-8] 


sd_der_analitica = -4*sinh(2*x)*(1 - tanh(2*x)**2)

for i in h:
    sd_der_numerica = (f(x + i) - 2*f(x) + f(x - i))/i**2
    scatter(x, sd_der_numerica, label = i)
title('Numérica(dot) versus Analítico')
xlabel('x')
ylabel('f^2(x)')
legend()

plot(x, sd_der_analitica, label = 'analitica')
legend()
show()   

"""
Podemos perceber que ao colocar o h = 1e-8 perdemos totalmente a precisão. Podemos concluir, portanto
que nosso método não possui uma precisão muito apreciável para cálculo de segunda derivada para funções
semelhantes a essas.

"""