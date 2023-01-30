# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:25:05 2019

@author: Bolsista
"""
from scipy.constants import G
import numpy as np
from gaussxw import gaussxwab
import matplotlib.pyplot as plt

def f(x, y, z):
        return (x**2 + y**2 + z**2)**(-3/2)


def DuploGauss(Nx, Ny, xa, xb, ya, yb, z):
    x, wi = gaussxwab(Nx, xa, xb)
    y, wj = gaussxwab(Ny, ya, yb)
    I = 0.0
    for i in range(Nx):
        for j in range(Ny):
            I += wi[i]*wj[j]*f(x[i], y[j], z)
    return I

# constantes
M = 1e4 #kg
L = 10 #m
sigma = M/L**2 #kgm^-2
#[G] = m^3kg^-1s^-2

# variáveis e pontos
Nx = 100; Ny = 100
z = np.linspace(0 , 10, 500)
xa = -L/2; xb = L/2
ya = -L/2; yb = L/2

# Duplo Gauss
S = DuploGauss(Nx, Ny, xa, xb, ya, yb, z)
Fz = G*sigma*z*S

plt.plot(z, Fz )
plt.xlabel('z')
plt.ylabel('Fz')
plt.show()

"""
O erro que observamos para valores pequenos de z decorre do método de Gauss que
estou utilizando para fazer a integração da curva dada. Contudo, talvez se mudarmos 
o método de integração podemos absorver esse erro. Por exemplo, utilizando
o método de Simpson. Eu tentei aumentar o valor de Nx = Ny =1000 mas não 
deu certo. Colocando z iniciando em 1, elimina-se o erro tbm.
"""