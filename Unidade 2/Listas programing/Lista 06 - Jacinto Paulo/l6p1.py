"""
Desenvolvido por: Jacinto Paulo
Disciplina: Física Computacional I
Prof.: Leonardo Dantas Machado

Lista 6 - Problema 1
"""

import numpy as np
import matplotlib.pyplot as plt

def P(x):
	return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1

def Pp(x):
	return 6*924*x**5 - 5*2772*x**4 + 4*3150*x**3 - 3*1680*x**2 + 3*420*x - 42

# Gráfico

"""
x = np.linspace(0, 1, 100)

plt.plot(x, P(x), label='o')
plt.title('Polinômio de Legendre 6ª ordem')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.grid()
plt.show()
"""
# Newton's method

# chute inicial --- Raízes Obtidas
"""
x = 0 ; x* = 0.16939530786880955
x = 0.4; x* = 0.6193095870239558
x = 0.9; x* = 0.9662347549773787

Para as outras três raízes o método diverge. A forma da curva não é favorável.

"""
x = 0.2

delta = 1 # e = x' - x ~ abs(delta) = f(x)/f'(x)

while(abs(delta) > 1e-10):
	delta = P(x)/Pp(x)
	x = x - delta

print(x)

