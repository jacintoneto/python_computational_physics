from numpy import loadtxt, linspace, log, mean
import matplotlib.pyplot as plt

dados = loadtxt('decay.data', float)

xd = dados[:,0] #time
yd = dados[:,1] #particles decay number
t = linspace(0,120, 500)

z = log(yd)
num = 0; den = 0.
for i in range(xd.size):
	num +=  xd[i]*(z[i] - mean(z))
	den += xd[i]*(xd[i] - mean(xd))

m = num/den
a = mean(z) - m*mean(xd)

def lnR(ap, mp, tp):
	return a + m*t

ajuste_z = lnR(a, m, t)

tau = -1/m
print("Vida média: ", tau)
plt.scatter(xd, z, label='z = log(yd)')
plt.plot(t, ajuste_z, label='z ajuste', color='orange')
plt.legend()
plt.xlabel('$Time\,(ns)$')
plt.ylabel('$log(y_{d})$')
plt.show()
