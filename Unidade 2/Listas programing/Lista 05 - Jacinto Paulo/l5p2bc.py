# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:08:39 2019

@author: Bolsista
"""

import numpy as np


def fx(x, y, a, b):
    return (b - a*y)/x 

def relaxacao(z, y, a, b):
    precisao = 1e-6
    zold = 0.0
    while(abs(z-zold) > precisao):
        zold = z
        z = fx(z, y, a, b)
    
    return z


a = 1; b = 2 
y = 1; x = 1

solZ = relaxacao(x, y, a, b)

print(solZ)

