"""
Desenvolvido por: Jacinto Paulo
Disciplina: Física Computacional I
Prof.: Leonardo Dantas Machado

Lista 6 - Problema 3 - Letra A, B
"""

import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab

# a)
hc = 1.23984193*10**3  # eV.nm
k = 8.6173303*10**-5 # eV.K^-1

def f(z):
	return z**3/(np.exp(z) - 1)

def eta(T):
	N = 100
	l1 = 390 # m
	l2 = 750 # m
	a = hc/(l2*k) + 1e-7
	b = hc/(l1*k) - 1e-7
	
	x, w = gaussxwab(N, a/T, b/T)
	I = 0.0
	for i in range(N):
		I += w[i]*f(x[i])

	return (15/np.pi**4)*I

T = np.linspace(300, 10000, 100)
n = list(map(eta, T))

plt.plot(T, n)
plt.title('Eficiência da Lâmpada')
plt.xlabel('$T$')
plt.ylabel('$\eta (T)$')
plt.grid()
plt.show()

# b)
precisao = 1 # 1K
z = (1 + np.sqrt(5))/2

# Valores Iniciais de T
T1 = 6500; T4 = 7500; T2 = T4 - (T4-T1)/z ; T3 = T4 + (T4-T1)/z
#Valores Iniciais da Função Eta
n1 = eta(T1); n2 = eta(T2); n3 = eta(T3); n4 = eta(T4)


# Computando o máximo
while(T4-T1 > precisao):
	if(n2 < n3):
		T4, n4 = T3, n3
		T3, n3 = T2, n2
		T2 = T4 - (T4-T1)/z
		n2 = eta(T2)
	else:
		T1, n1 = T2, n2
		T2, n2 = T3, n3
		T3 = T1 + (T4-T1)/z
		n3 = eta(T3)

T_max = 0.5*(T1 + T4)
print("Temperatura de eficiência máxima: ", T_max)

# c)
"""
Torna-se ineficiente utilizar lâmpadas de tungstênio devido seu pico de temperatura máxima ser muito alto. Supera a própria temperatura de fusão do material e a temperatura da superfície do Sol! Nesses termos, não é nada prático. 
"""
