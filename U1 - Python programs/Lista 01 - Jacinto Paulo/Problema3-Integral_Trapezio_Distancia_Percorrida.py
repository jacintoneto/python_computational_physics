# Desenvolvido por: Jacinto Paulo da Silva Neto
# Problema 3 - Integral Númerica - Método do Trapézio em Distância Percorrida
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("velocities.txt", float)
t = data[:, 0]
v = data[:, 1]

#area do trapézio = distância percorrida em casa ponto --> S = (b+B)h/2, sendo h = t, b = v[0] e B = v[99] = v[-1].

D = (abs(v[0]) + abs(v[-1]))/2 
N = np.size(v) 		# np.size(v) ou np.size(t)

# a)
for i in range(1, N-1):
	D += abs(v[i]) 

# Novamente, considera-se a "Distância Percorrida efetiva = |\delta S_1| + ... + |\delta S_N|", onde (\delta S) = V_m * (\delta t)  e (\delta t) = 1s.
print("\nA distância aproximada percorrida será: ", D)

# b)
# velocidade versus tempo
plt.plot(t,v)
plt.xlabel("Tempo [s]")
plt.ylabel("Velocidade [m/s]")
plt.title("Velocidade x Tempo")
plt.show()

# distância percorrida versus tempo

d = np.empty(N, float)
d[i] = 0 # afim de determinar o ponto inicial que d começa a receber valores com sentido

for i in range(1, N-1):
	d[i+1] = d[i] + abs(v[i] + v[i+1])/2

plt.plot(t, d)
plt.xlabel("Tempo [s]")
plt.ylabel("Distância Percorrida [m]")
plt.title("Distância Percorrida x Tempo")
plt.show()

