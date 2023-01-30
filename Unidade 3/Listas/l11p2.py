"""
Desenvolvido por: Jacinto Paulo
Professor: Leonardo Machado
Disciplina: Física Computacional I
Lista 11 - Problema 2 - Leapfrog Method
"""

from numpy import array, arange
import matplotlib.pyplot as plt

# Condições Iniciais etc
h = 0.001
x0 = 1; fx0 = 0
ti = 0; tf = 50

def f(r,t):
    x = r[0]
    fx = r[1]
    ffx = fx**2-x-5
    return array([ fx, ffx], float)

r = array([x0, fx0] , float)
tpoints = arange(ti, tf, h)
xpoints = []

#Leapfrog Method
for t in tpoints:
    xpoints.append(r[0])
    rmid = r + 0.5*h*f(r, t) # r(t + 0.5h) = r(t) + 0.5hf(r(t), t) --> obtained applying Euler's method for half step size.
    r = r + h * f(rmid, t) # r(t + h) = r(t) + hf(r(t + 0.5h), t + 0.5h)

plt.plot(tpoints, xpoints, 'c')
plt.title('Leapfrog Method')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.show()
