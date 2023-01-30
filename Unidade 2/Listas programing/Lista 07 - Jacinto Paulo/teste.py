# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:50:54 2019

@author: Bolsista
"""

import numpy as np


def relX(z, a, b):
    precisao = 1e-6
    zold = 0.0
    
    while(abs(z-zold) > precisao):
        zold = z
        z = fx(z, a, b)

    return z

def relY(w, a, b):
    precisao = 1e-6
    wold = 0.0
    
    while(abs(w-wold) > precisao):
        wold = w
        w = fy(w, a, b)
    
    return w

def fy(x, a, b):
    return b/(x**2 + a)

def fx(y, a, b):
    return y*(a + x**2) 


a = 1; b = 2 
y = 0.5; x = 0.5

solX = relX(x, a, b)
solY = relY(y, a, b)

print(solX, solY)