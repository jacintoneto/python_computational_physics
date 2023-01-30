from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from numpy import loadtxt, empty, linspace, arange

# Importando os dados do arquivo scattering.data
dados = loadtxt("scattering.data", float)
xd = dados[:,0]
yd = dados[:,1]
erro = dados[:,2]

N = linspace(0, 200, 200)

### PARTE 1 ####
flinha = interp1d(xd, yd)
listalinha = []

### PARTE 2 ####
f = interp1d(xd, yd, kind='cubic')
lista = []

for i in N:
	lista.append(f(i))

for i in N:
	listalinha.append(flinha(i))

plt.plot(N, listalinha, label = "Interpolação linear", color="orange")
plt.scatter(xd, yd,label = "Dados experimentais")
plt.legend()
plt.xlabel("Energia(MeV)")
plt.ylabel("Seção Transversal")
plt.show()

plt.clf() #cleaf
plt.subplot()
plt.plot(N, lista, label = "Interpolação linear", color="orange")
plt.scatter(xd, yd,label = "Dados experimentais")
plt.legend()
plt.xlabel("Energia(MeV)")
plt.ylabel("Seção Transversal")
plt.show()