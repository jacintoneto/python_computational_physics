# Programa que calcula integrais usando a regra de Simpson
from numpy import exp

def f(z):
    return exp(-z**2/(1-z)**2)/(1-z)**2

def w(k,N):
    if k==0 or k==N:
        return 1/3
    elif (k%2)==0:
        return 2/3
    else:
        return 4/3

def integral(a,b,N):
    h = (b-a)/N
    soma = 0.0
    for k in range(N+1):
        soma += w(k,N)*f(a+k*h)
    return h*soma

a = 0.0
b = 1.0-1e-16
N = 1000
integ = integral(a,b,N)

print("Para um número de fatias",N,"o valor estimado da integral é",integ,".")

