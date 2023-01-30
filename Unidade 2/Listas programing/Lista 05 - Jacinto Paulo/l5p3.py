# -*- coding: utf-8 -*-
"""
Disciplina: Física Computacional I
Autor: Jacinto Paulo da Silva Neto
Professor: Leonardo Dantas Machado

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k
def f(z):
    return (5*np.exp(-z) + z - 5)

prec = 1e-6
x1 = 7
x2 = 2
# checking the sign agreement 
print("A função em f(x1): ", f(x1), "\nA função em f(x2): ", f(x2))

while(abs(x2-x1) > prec):

    xp = (x1+x2)/2
        
    if (f(xp)*f(x1) > 0):
        x1 = xp
    else:
        x2 = xp
        
x = (x1+x2)/2 #no dimension
b = h*c/(k*x) #m.K
print("\nRaíz: ", x, "\nConstante de deslocamento de Wein: ", b)

# Estimando a temperatura na superfície do Sol
l = 502*10**(-9) #m
T = b/l #K

print("\nTemperatura: ", T)
