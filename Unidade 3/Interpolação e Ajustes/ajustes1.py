from numpy import loadtxt, exp, linspace
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def func(x,a,b):
	return a*exp(-b*x)

dados = loadtxt('decay.data', float)

xd = dados[:,0] #time
yd = dados[:,1] #particles decay number

param, pcov = curve_fit(func, xd, yd)
# a e b estão contidos na variável 'param'. param[0] = a \equiv initial , param[1] = b \equiv $\tau$ \equiv vida média.

# $R = \frac{dN}{dt}$ as well as $R_0 = \frac{dN_{0}}{dt}$

R_0 = param[0]; lamb = param[1]
time = linspace(0, 120, 500)
R = func(time, R_0 , lamb) 

plt.scatter(xd, yd, label='Dados')
plt.plot(time, R, label='Ajustes', color='orange')
plt.legend()
plt.xlabel('$Time\,(ns)$')
plt.ylabel('$N$ (particle number)')
plt.title('Pion decay')
plt.show()

#Vida média $\lamb = 1/\tau = param[1]$
tau = 1/lamb
print("Vida média: ", tau)