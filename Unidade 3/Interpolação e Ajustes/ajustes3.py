# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:03:28 2019

@author: Bolsista
"""

from pylab import errorbar, plot, show, scatter, xlabel, ylabel, legend, title
from numpy import loadtxt,linspace
from scipy.optimize import curve_fit

dados = loadtxt('scattering.data', float)
xd = dados[:,0] # energy
yd = dados[:,1] # transversal cross section
erro = dados[:,2]

def func(E, Er, G, fr): # Er:ressonace energy, Gamma:total level energy size
	return	fr**2/((E-Er)**2 + (G/2)**2)

param, pcov = curve_fit(func, xd, yd)
E_r, Gamma, f_r = param[0], param[1], param[2]

En = linspace(0, 200, 200)
f = func(En, E_r, Gamma, f_r)

print("Energia de ressonância: ", E_r, "\n\nLargura do Nível de Energia: ", Gamma)

plot(En, f, label = "Ajuste de Dados", color="orange")
scatter(xd, yd, label = "Dados experimentais")
legend()
title("Espalhamento de nêutrons")
xlabel("Energia(MeV)")
ylabel("Seção Transversal")
show()


# -------------------------------------------------------------------------------------------------

param, pcov = curve_fit(func, xd, yd)		
flinha = func(En, E_r, Gamma, f_r)

plot(En, flinha, label = "Ajuste de Dados", color="orange")
scatter(xd, yd,label = "Dados experimentais")
legend()
title("Espalhamento de nêutrons")
xlabel("Energia(MeV)")
ylabel("Seção Transversal")
errorbar(xd, yd, yerr = erro, fmt='o', capsize=5)
show()

"""
# d) A barra não auxilia a visualizar a precisão das medidas uma vez que as barras de erro estão desproporcionais.
# e) O valor para Er se aproximou ainda mais do valor previsto teoricamente. Gamma aumentou também,
mas se distanciou do valor teorizado. 
"""
# -------------------------------------------------------------------------------------------------
param, pcov = curve_fit(func, xd, yd, sigma = erro)	
E_r, Gamma, f_r = param[0], param[1], param[2]
print("Energia de Ressonância: ", E_r,"\n\nLargura do Nível de Energia: ", Gamma)

f2linha = func(En, E_r, Gamma, f_r)

plot(En, f2linha, label = "Ajuste de Dados", color="orange")
scatter(xd, yd,label = "Dados experimentais")
legend()
title("Espalhamento de nêutrons")
xlabel("Energia(MeV)")
ylabel("Seção Transversal")
show()


