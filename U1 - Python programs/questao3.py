# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:52:48 2019

@author: Luanna Karen
"""

# Funções de onda do oscilador harmônico

import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def H(n,x): # Polinômios de Hermite
    if (n == 0):
        return 1;
    elif (n == 1):
        return 2*x;
    else:
        return 2*x*H(n-1,x) - 2*(n-1)*H(n-2,x);

def psi(n,x):
    fat = factorial(n);
    c = 1/np.sqrt(2**n * fat * np.sqrt(np.pi));
    return(c*np.exp(- x**2/2)*H(n,x));

x = np.linspace(-2,2,1000);

#Polinômios de Hermite

H1 = H(1,x);
H2 = H(2,x);
H3 = H(3,x);    
H4 = H(4,x);

plt.plot(x,H1,label="H1(x)");  
plt.plot(x,H2,label="H2(x)");  
plt.plot(x,H3,label="H3(x)");  
plt.plot(x,H4,label="H4(x)"); 

plt.xlabel("x");
plt.ylabel("Hn(x)"); 
plt.title("Polinônios de Hermite")
plt.legend();
plt.show();

plt.clf();

x = np.linspace(-4,4,1000);

# Funções de onda

psi0 = psi(0,x);
psi1 = psi(1,x);
psi2 = psi(2,x);
psi3 = psi(3,x);

plt.plot(x,psi0,label="psi_0(x)");  
plt.plot(x,psi1,label="psi_1(x)");
plt.plot(x,psi2,label="psi_2(x)");  
plt.plot(x,psi3,label="psi_3(x)"); 

plt.xlabel("x");
plt.ylabel("psi_n(x)"); 
plt.title("Funções de onda do Oscilador Harmônico Quântico")
plt.legend();
plt.show();

plt.clf();

x = np.linspace(-10,10,1000);
psi30 = psi(30,x);

plt.plot(x,psi30); 
plt.xlabel("x");
plt.ylabel("psi_30(x)"); 
plt.title("Função de onda do Oscilador Harmônico Quântico n = 30")
plt.show();

# Implementando a quadratura Gaussiana

def gaussxw(N):

    # Aproximação inicial para as raízes dos polinômios de Legendre
    a = np.linspace(3,4*N-1,N)/(4*N+2);
    x = np.cos(np.pi*a+1/(8*N*N*np.tan(a)));

    # Encontrando as raízes pelo método de Newton
    tol = 10**(-15);
    erro = 100.0;
    while (erro > tol):
        P0 = np.ones(N,float);
        P1 = np.copy(x);
        for k in range(1,N):
            P0,P1 = P1,((2*k+1)*x*P1-k*P0)/(k+1);
        dP = (N+1)*(P0-x*P1)/(1-x**2);
        dx = P1/dP;
        x = x - dx;
        erro = np.max(abs(dx));

    # Calculando os pesos
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dP**2);

    return x,w;

def gaussxwab(N,a,b):
    x,w = gaussxw(N);
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w;

def f(z):
    x = z/(1-z**2);
    n = 5;
    return x**2 * psi(n,x)**2 * (1 + z**2)/(1 - z**2)**2;

def integral(N,a,b):
    x,w = gaussxwab(N,a,b);
    return np.sum(w*f(x));   


a = -1 + 10**(-10);
b = 1 - 10**(-10);
N = 100;

I = integral(N,a,b);

print("\n * valor da incerteza quântica:",np.sqrt(I));




















