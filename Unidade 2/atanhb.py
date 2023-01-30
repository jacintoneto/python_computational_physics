from numpy import cosh, tanh, linspace
from pylab import plot, show, axhline, axvline, grid

def f(x):
    return tanh(x) -u

def df(x):
    return 1.0/cosh(x)**2

def newton(x,xold):
    while (abs(x-xold)>eps):
        xold = x
        x = x - f(x)/df(x)
    return(x)

upoints = linspace(-0.99,0.99, 100)
eps = 1.0e-12
xpoints = []

for u in upoints:
    x = newton(0.0,10.0)
    xpoints.append(x)

plot(upoints,xpoints)
axhline(y = 0,linestyle='-',color='black')
axvline(x = 0,linestyle='-',color='black')
grid('true')
show()
