
from __future__ import division, print_function
from os import sys
from numpy import exp,linspace
from pylab import *
sys.path.append('cpresources')
from gaussxw import gaussxw

N = 10
x,w = gaussxw(N)


f = lambda x: x**4*exp(x)/(exp(x)-1)**2

T = 5
tetaD = 428 #K
ro = 6.022e28 #m^-3
V = 1000
kb = 1.38e-23

def cv(T):
	
	a = 0
	b = tetaD/T 
	xp = 0.5*(b-a)*x + 0.5*(b+a)
	wp = 0.5*(b-a)*w
	const = 9*V*ro*kb*(T/tetaD)**3	
	s = sum(f(xp)*wp)

	return s*const

T = linspace(5,500,100)
C = [cv(Ti) for Ti in T]
plot(T,C)
xlabel('Temperature, K')
ylabel('C_v')
show()
