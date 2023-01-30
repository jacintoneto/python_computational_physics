from numpy import zeros, pi
from numpy.linalg import eigh

e = 1.6022e-19
M = 9.1094e-31
L = 5e-10
a = 10*e
hbar = 1.0545718e-34

def V(m,n):
    if m == n:
        return (L**2)/4
    elif( (m%2==0 and n%2==0) or (m%2==1 and n%2==1) ):
        return 0.0
    else:
        return -((2*L)/pi)**2 * ((m*n)/(m**2-n**2)**2)

def K(m,n):
    if m==n:
        return ((hbar**2)/(2*M)) * ((n**2*pi**2)/(L**2))
    else:
        return 0.0

def H(m,n):
    return K(m,n) + ((2*a)/L**2) * V(m,n)


