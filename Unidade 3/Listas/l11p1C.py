"""
Desenvolvido por: Jacinto Paulo
Professor: Leonardo Machado
Disciplina: Física Computacional I
Lista 11 - Problema 1 - Órbitas de Cometas
Letra C
"""

from numpy import array, arange, sqrt
import pylab as pl

# Constantes do sistema
M = 1.9891e30 # kg
G = 66374.2  # m^3.kg^-1*anos^-2
k = M*G

ti = 0; tf = 165 # anos
delta = 1000 # precisão m.ano^-1 
N = 150000
h = (tf - ti)/N

# Condições Iniciais
x0 = 4e12; y0 = 0 # m 
vx0 = 0; vy0 = 15768000000 # m.ano^-1

def f(r, t):
	x, y, vx, vy = r
	R = sqrt(x**2 + y**2)
	ax = -k*x/R**3
	ay = -k*y/R**3
	return array([vx, vy, ax, ay], float)

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

	#calulando erro @ 'r1 e r2'
	x1 = r1[0]
	y1 = r1[1]
	x2 = r2[0]	
	y2 = r2[1]
	erro = sqrt((x1**2 - x2**2)**2 + (y1- y2)**2)/30 # Euclidian error

	# calculando rho e fator multiplicativo de h' = h*rho
	rho = h*delta/erro
	gamma = rho**(1/4)


## condições sobre rho associado ao tamanho do passo encontrar a precisão
	# 1. precisão alvo encontra h, então vamos para o próximo passo
	if(rho >= 1):
		# atualiza t
		t = t + 2*h 
		# garante h não muito grande
		if(gamma > 2): 
			h *= 2
		else:
			h *= gamma
		r1[0] += (x1 - x2)/15
		r1[1] += (y1 - y2)/15
		return r1, h, t
	# 2. precisão NÃO enontra h, então voltamos para o passo anterior com um h menor
	else:
		return adaptative_step(r, t, gamma*h)
tpoints = []
xpoints = [] 
ypoints = [] 
r = array([x0, y0, vx0, vy0], float) 
t = ti

while(t < tf):
	tpoints.append(t)
	xpoints.append(r[0])
	ypoints.append(r[1])
	var_r, h, t = adaptative_step(r, t, h)
	r += var_r

xp = array(xpoints, float)/1000
yp = array(ypoints, float)/1000
pl.plot(xp, yp, 'c')
pl.title('Órbita de Cometas - Método Passo Adaptativo')
pl.xlabel('$x(km)$')
pl.ylabel('$y(km)$')
pl.show()

"""
Com relação a velocidade o RK4 é bem mais rápido, contudo a precisão do adaptativo é muito maior. Podemos afirmar isso através da largura estimada da trajetória no gráfico. Vemos que para o mesmo N=150k nos dois métodos, obtemos para o RK4 um erro notável no fechamento da órbita. Ou seja, seria necessário aumentar o valor de N para que a precisão do RK4 aumentasse. Ainda com N = 200k percebemos o mesmo erro no fechamento da órbita. Quando aumentamos o número de passos para N = 500k e N = 1000k é simplesmente não notável a alteração da precisão, apesar de nos dois casos a órbita é fechada. Além disso, o tempo que leva computando o resultado também aumenta. Logo, para este caso, o método adaptativo é mais conveniente que o RK4.
"""
