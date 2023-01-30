# Programa que calcula integrais usando a regrado trapézio adaptativa
from numpy import sin, sqrt
from gaussxw import gaussxw

def f(x):
    return sin(sqrt(100*x))**2

a = 0.0
b = 1.0
N = 50
y,w = gaussxw(N)
x = ((b-a)/2)*y+(b+a)/2
wl = ((b-a)/2)*w
integ = 0.0

for k in range(N):
    integ+=wl[k]*f(x[k])

print("Para um número de fatias",N,"o valor estimado da integral é",integ,".")


