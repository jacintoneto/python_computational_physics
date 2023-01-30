# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:52:21 2019

@author: Bolsista
"""
import numpy as np

def f(x):
    return (1 - np.exp(-c*x))

precisao = 1e-6
xold = 0
x = 1 #chute
c = 2
i=0
while(abs(x - xold) >= precisao):    
    xold = x
    x = f(x)    
    erro = abs(x - xold)
    passo = i
    print(passo, x, erro)
    i+=1
