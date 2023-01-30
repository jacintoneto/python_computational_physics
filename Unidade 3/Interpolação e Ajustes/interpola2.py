from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from numpy import loadtxt, empty, linspace, arange

def fun(x, a, b, fa, fb):
	return (fa*(b-x) + fb*(x-a))/(b-a)

# Importando os dados do arquivo scattering.data
dados = loadtxt("scattering.data", float)
xd = dados[:,0]
yd = dados[:,1]
erro = dados[:,2]

n = len(xd)
listaf = []
listax = []

for i in range(n-1):
	a = xd[i]; b = xd[i+1]
	fa = yd[i]; fb = yd[i+1]
	
	for i in linspace(a, b, 25): 
		listaf.append(fun(i, a, b, fa, fb))
		listax.append(i)

plt.plot(listax, listaf, color='orange')
plt.scatter(xd, yd)
plt.show()