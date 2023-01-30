"""
Desenvolvido por: Jacinto Paulo
Professor: Leonardo Machado
Disciplina: Física Computacional I
Lista 11 - Problema 3 - Verlet Method
"""

from numpy import array, arange, sqrt
import matplotlib.pyplot as plt


# Constantes
G = 6.6738e-11*(8760*3600)**2 # m^3.kg−1.ano^-2
M = 1.9891e30  # kg
m = 5.9722e24  # kg
k = G*M

# Condições Iniciais
x0 = 1.4710e11 # m
vx0 = 0
y0 = 0
vy0 = 3.0287e4*8760*3600 # m.ano^-1

t0 = 0
tf = 4  # ano
h = 1/8760  # h em anos

def f(r): # f independe explicitamente de t
    x = r[0]
    vx = r[1]
    y = r[2]
    vy = r[3]
    R = sqrt(x**2 + y**2)
    return array([ vx, -k*x/R**3, vy, -k*y/R**3 ], float)


tpoints = arange(t0, tf, h)
xpoints = []
ypoints = []
E_cinetica = []
E_potencial = []
r = array([x0, vx0, y0, vy0], float)

## Verlet method ##
# 1º Estima velocidades no ponto v(t + 0.5h)
fmid = 0.5*h*f(r)
vxmid = r[1] + fmid[1]
vymid = r[3] + fmid[3]

# 2º Repete sucessivas x(t + h) = x(t) + hv(t +0.5h) e v(t + 1.5h) = v(t + 0.5h) + hf(x(t + h), t +h)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[2])
    E_cinetica.append(0.5*m*(r[1]**2 + r[3]**2)/(8760*3600)**2)
    E_potencial.append(-6.6738e-11*M*m/sqrt(r[0]**2 + r[2]**2))

    # atualizando posições
    r[0] += h*vxmid 
    r[2] += h*vymid 

    # atualizando velocidades
    w = h*f(r) 
    r[1] = vxmid + 0.5*w[1] 
    r[3] = vymid + 0.5*w[3]
    fmid = 0.5*h*f(r)
    vxmid += w[1]  
    vymid += w[3]



plt.plot(xpoints, ypoints)
plt.title('Órbita da Terra')
plt.xlabel('$x$ (m)')
plt.ylabel('$y$ (m)')
plt.show()
plt.clf()

E_total = array(E_cinetica, float) + array(E_potencial, float)

plt.plot(tpoints, E_cinetica, color = 'c', label = 'T')
plt.plot(tpoints, E_potencial, color = 'orange', label = 'V')
plt.plot(tpoints, E_total, color = 'blue', label = '$E_t = T + V$')
plt.title('Energias do Sistema')
plt.legend()
plt.xlabel('$t$ (anos)')
plt.ylabel('$E$ (Joules)')
plt.show()
