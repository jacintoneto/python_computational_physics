"""
Desenvolvido por: Jacinto Paulo
Disciplina: Física Computacional I
Prof.: Leonardo Dantas Machado

Lista 6 - Problema 2
"""

import numpy as np
import matplotlib.pyplot as plt


def L1(x):
	return	G*M/x**2 - G*m/(R - x)**2 - x*w**2

def L1p(x):
	return -2*(G*M/r**3 + G*m/(R - r)**3) - w**2

G = 6.674e-11 #m^3.kg^-1.s^-2
M = 5.974e24 #kg
m = 7.348e22 #kg
R = 3.844e8 #m
w = 2.662e-6 #s⁻1

# ploting the function
"""
r = np.linspace(-10,10,1000)

plt.plot(r, L1(r))
plt.title('Ponto de Lagrange')
plt.xlabel('r')
plt.ylabel('L1(r)')
plt.grid()
plt.show()
"""

r = 3e5 # chute
delta = 1
i = 0 
while ((abs(delta) > 1e-10) and (i < 500)):
	delta = L1(r)/L1p(r)
	r -= delta
	i += 1

print("O ponto de Lagrange: ", r, "m\n L = ", L1(r))

