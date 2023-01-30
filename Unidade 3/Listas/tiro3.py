from numpy import array
from pylab import plot,show

def f(r,t):
    y,v = r[0],r[1] 
    fy = v
    fv = -g
    return array([fy,fv])

def RK4(r,t):
    k1 = h*f(r,t)
    k2 = h*f(r+k1/2,t+h/2)
    k3 = h*f(r+k2/2,t+h/2)
    k4 = h*f(r+k3,t+h)
    return r + (1/6)*(k1+2*k2+2*k3+k4)

def solve(v0):
    t = a
    r = array([y0, v0])
    while (t < b):
        r = RK4(r, t)
        t += h
    return r[0] 

# Parâmetros
a,b = 0, 10
g = 9.8
y0= 0
tol = 1e-6
N = 1000
h = (b-a)/N
v1,v2 = 10,100
# Resolução
y1, y2 = solve(v1),solve(v2)
while(abs(v2-v1)>tol):
    vnew = (v1 + v2)/2
    ynew = solve(vnew)
    if (ynew*y1>0):
        y1,v1 = ynew, vnew
    else:
        y2, v2 = ynew, vnew

print("A velocidade inicial que deve ser fornecida a bola para que ela retorne ao solo no tempo t = 10 s é", vnew)

