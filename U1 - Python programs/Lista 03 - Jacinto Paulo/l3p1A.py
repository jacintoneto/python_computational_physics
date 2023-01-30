"""
Desenvolvido por: Jacinto Paulo da Silva Neto
Disciplina: Física Computacional I
Prof.: Leonardo Dantas Machado

Lista 3 - Problema 1 Letra A - Calor Específico de um Sólido
"""
import matplotlib.pyplot as plt
from math import *
import numpy as np
from gaussxw import gaussxw

def f(x):
	return ((x**4)*exp(x))/(exp(x) - 1)**2

def gauss(N):
	x, w = gaussxw(N)
	xp = 0.5*(b-a)*x + 0.5*(b+a)
	wp = 0.5*(b-a)*w
	I = 0.0
	for i in range(N):
		I+= wp[i]*f(xp[i])
	return I

def Cv(T):
	const = 9*V*rho*kB*(T/tetaD)**3
	return const*gauss(N)

# Constantes e Parâmetros de Integração ----------------

rho =6.022e28	#densidade de átomos (m^-3)
V = 1e-3	#volume do sólido (m^3)
kB = 1.38e-23  #constante de Boltzmann (JK^-1)
T = float(input("\n>> Informe a temperatura do material: "))
tetaD =	428 #temperatura de Debye(K)
N = 50
a = 0
b = tetaD/T

Calor = Cv(T)
print("\n O calor específico: ", Calor)

