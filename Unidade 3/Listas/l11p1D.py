"""
Desenvolvido por: Jacinto Paulo
Professor: Leonardo Machado
Disciplina: Física Computacional I
Lista 11 - Problema 1 - Órbitas de Cometas
Letra D
"""

from numpy import array, arange, sqrt
import pyplot as pl

# Constantes do sistema
M = 1.9891e30 # kg
G = 66374.2  # m^3.kg^-1*anos^-2
k = M*G

# Condições Iniciais
x0 = 4e12
y0 = 0 # m 
vx0 = 0
vy0 = 15768000000 # m.ano^-1
ti = 0
tf = 165 # anos

def f(r, t):
	x, y, vx, vy = r
	R = sqrt(x**2 + y**2)
	ax = -k*x/R**3
	ay = -k*y/R**3
	return array([vx, vy, ax, ay], float)


"""
Método do RK4 com h fixo
"""
N = 200000
h = (tf - ti)/N
tpoints = arange(ti, tf, h)
xpoints = []
ypoints = [] 
r = array([x0, y0, vx0, vy0], float)

for t in tpoints:
	xpoints.append(r[0])
	ypoints.append(r[1])
	k1 = h*f(r, t)
	k2 = h*f(r+k1/2, t+h/2)
	k3 = h*f(r+k2/2, t+h/2)
	k4 = h*f(r+k3, t+h)
	r += (k1+2*k2+2*k3+k4)/6

"""
pl.plot(x, y,'.', color='c')
pl.legend()
pl.xlabel('$x(km)$')
pl.ylabel('$y(km)$')
pl.title('Órbitas de Cometas - Método RK4')
pl.show()
"""

"""
Método de Passo Adaptativo
"""
delta = 1000 # precisão alvo por unidade de intervalo em m.yr^-1 
N = 150000
h = (tf - ti)/N # tamanho inicial do passo

def adaptative_step(r, t, h):
	def RK_estimate_step(r, t, h):
		k1 = h*f(r, t)
		k2 = h*f(r+k1/2, t+h/2)
		k3 = h*f(r+k2/2, t+h/2)
		k4 = h*f(r+k3, t+h)
		return (k1+2*k2+2*k3+k4)/6

	# dois passos h --> r1 @ r(t +2h)
	step_1 = RK_estimate_step(r, t, h) 
	step_2 = RK_estimate_step(r+ step_1, t+h, h)
	r1 = step_1 + step_2 # vetor variado na posição e velocidades

	# único 2h --> r2 @ r(t +2h)
	r2 = RK_estimate_step(r, t, 2*h) # vetor variado na posição e velocidades

	#calulando erro @ r1 e r2
	x1 = r1[0]
	y1 = r1[1]
	x2 = r2[0]	
	y2 = r2[1]
	erro = sqrt((x1**2 - x2**2)**2 + (y1- y2)**2)/30 # Euclidian error

	# calculando rho e fator multiplicativo
	rho = h*delta/erro
	gamma = rho**(1/4)

## condições sobre rho associado ao tamanho do passo encontrar a precisão alvo
	# precisão alvo encontra h, então vamos para o próximo passo
	if(rho >= 1):
		# atualiza t
		t = t + 2*h 
		# garante h não muito grande
		if(gamma > 2): 
			h *= 2
		else:
			h *= gamma
		# local extrapolation
		r1[0] += (x1 - x2)/15
		r1[1] += (y1 - y2)/15
		return r1, h, t
	# precisão alvo NÃO enontra h, então voltamos para o passo anterior com um h menor
	else:
		return adaptative_step(r, t, gamma*h)

tpoints = []
xppoints = []
yppoints = [] 
r = array([x0, y0, vx0, vy0], float) 
t = ti
while(t < tf):
	tpoints.append(t)
	xppoints.append(r[0])
	yppoints.append(r[1])
	var_r, h, t = adaptative_step(r, t, h)
	r += var_r

pl.scatter(array(xpoints, float), array(ypoints, float), color='b', label='RK4')
pl.scatter(array(xppoints, float)[::20], array(yppoints, float)[::20], color='r', label='Adaptative')
pl.legend()
pl.title('Órbita de Cometas')
pl.xlabel('$x (km)$')
pl.ylabel('$y (km)$')
pl.show()
