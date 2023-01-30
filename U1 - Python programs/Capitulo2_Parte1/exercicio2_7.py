# Exercício 2.7: Altitude de um satélite
G = 6.67*10**(-11)#m³Kg⁻¹s⁻²
M = 5.97*10**(24) #Kg
R = 6371**(3) #m

from math import *

print("Um satelite deve ser lançado em uma órbita circular em torno da Terra, de modo que ele orbite o planeta uma vez a cada T segundos.\n\n")

escolha = int(input("Como você deseja informar o período T?\n 1- Segundos;\n 2 - Minutos; \n 3 - Horas.\n\nSua escolha: "))

if(escolha==1): #doenst need a transform
	T = float(input("\n\nInforme o valor do período T em segundos: "))
	h = ((G*M*T**2)/4*pi**2)**(1/3) - R
	print("\n\nA altitude do satélite será:", h, " m")

if(escolha==2): #transform minutos into seconds
	Tm = float(input("\n\nInforme o valor do período T em minutos: "))
	T = Tm*60
	h = ((G*M*T**2)/4*pi**2)**(1/3) - R
	print("\n\nA altitude do satélite será:", h, " m")

if(escolha==3): #transform hours into seconds
	Th = float(input("\n\nInforme o valor do período T em horas: "))
	T = Th*3600
	h = ((G*M*T**2)/4*pi**2)**(1/3) - R
	print("\n\nA altitude do satélite será:", h, " m")
