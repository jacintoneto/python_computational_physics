"""
Desenvolvido por: Jacinto Paulo 
Disciplina: Física Computacional I
Professor: Leonardo 

Lista 8 - Problema 1

"""

from numpy import empty, zeros, array, exp, real, cos, append
from vpython import *
from thomasjackalg import thomasjackalg

# Parâmetros do cálculo
N = 26
m, C, k , w = 1, 1, 6, 2
alfa = -m*w**2+2*k

# Vamos criar agora a matriz a ser resolvida
A = zeros([N,N],float)
v = zeros(N,float)
v[0] = C

for i in range(N):
    if (i == 0):
        A[i,i] = alfa - k
        A[i,i+1]= -k
    elif (i == (N-1)):
        A[i,i] = alfa -k
        A[i,i-1] = -k
    else:
        A[i,i] = alfa
        A[i,i-1] = -k
        A[i,i+1] = -k

# Algoritmo de Thomas-Jack
x = thomasjackalg(A, v)

# Animação do vpython
particles = empty(N, sphere)
delta =  2

for i in range(N):
    position = delta*(i - x.size/2)
    particles[i] = sphere(pos=vector(position, 0, 0), radius = 0.4)
        
dt = 0.1
t = 0
while(t < 1000):
    rate(10) #1/t
    for k in range(len(x)):
        position =  delta*(k - x.size/2) + x[k]*cos(w*t) #real(x[k]*exp(w*t))
        particles[k].pos = vector(position, 0, 0)
    t+=dt
