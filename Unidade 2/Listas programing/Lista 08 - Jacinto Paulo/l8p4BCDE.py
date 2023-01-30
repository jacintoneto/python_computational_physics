"""
Desenvolvido por: Jacinto Paulo 
Disciplina: Física Computacional I
Professor: Leonardo 

Lista 8 - Problema 4 - Letras B, C, D e E

"""
from numpy import zeros, pi, sin, sqrt, linspace
from numpy.linalg import eigh, eigvalsh
from matplotlib.pyplot import plot, legend, xlabel, ylabel, title, show

def H(m,n): 
    if (m==n): # diagonal
        return hbar_c**2*pi**2*n**2/(2*L**2*Mc2) + 0.5*a #(h*c)**2*pi*n**2/(4*Mc2*L**2) + 0.5*a

    elif (m%2==0 and n%2==0) or (m%2!=0 and n%2!=0):  # mesma paridade
        return 0

    else:  # diferentes paridades
        return -8*a/pi**2 * m*n/(m**2 - n**2)**2

def MatrizH(N):
	h = zeros([N,N], float)
	for m in range(1,N+1):
        	for n in range(1,N+1):
        	    h[m-1,n-1] = H(m,n)
	return h

# constantes
hbar_c = 197.32697e-9 # eV.m
Mc2 = 0.511e6 # eV
L = 5e-10 # m
a = 10 # eV

# Autovalores para ordem 10
N10 = 10 # Ordem da matrix H
MatrixH10 = MatrizH(N10) 
E10 = eigvalsh(MatrixH10)
print("------Ordem 10------\n\nAutovalores: \n", E10)

#E10, psi10 = eigh(MatrixH10)
# print("Matriz H:\n ", MatrixH10)
# print("\n\nAutovetores: \n", E10)


# Autovalores para ordem 100
N100 = 100 # Ordem da matrix H
MatrixH100 = MatrizH(N100)
MatrixH10 = MatrizH(N10) 
E100 = eigvalsh(MatrixH100)  
print("\n\n-----Ordem 100------\n\nAutovalores: \n", E100[:10]) # tomar até o 10º elemento

#E100, psi100 = eigh(MatrixH100)
# print("Matriz H:\n ", MatrixH100)
# print("\n\nAutovetores: \n", psi100)

"""
A precisão variou um pouco. Podemos ver que começa a aparecer valores um pouco distintos a partir da 5ª casa após a vírgula.
"""

# ------------------ trabalhando com a função de onda -------------------

# Psi não normalizada
def Psi(x, psi): 
	S = 0
	for n in range(len(psi)):
		S+= psi[n]*sin(pi*(n+1)*x/L)
	return S

N = 10
MatrixH = MatrizH(N)
E, psi = eigh(MatrixH)
x = linspace(0, L, 500)

plot(x, (Psi(x, psi[:,0]))**2, label='$|\psi_0(x)|^2$')
plot(x, (Psi(x, psi[:,1]))**2, label='$|\psi_1(x)|^2$')
plot(x, (Psi(x, psi[:,2]))**2, label='$|\psi_2(x)|^2$')
legend()
title('$|\psi_n(x)|^2$ - Não Normalizada')
xlabel('x')
ylabel('$|\psi_n(x)|^2$')
show()

# Psi normalizada <Psi|Psi> = 1, a demonstração está em latex
def NPsi(x,psi):
	soma_psin = 0
	for n in range(len(psi)):
		soma_psin += psi[n]**2
	C = sqrt(2/(L*soma_psin))

	return C*Psi(x,psi)

plot(x, (NPsi(x,psi[:,0]))**2, label='$|\psi_0(x)|^2$')
plot(x, (NPsi(x,psi[:,1]))**2, label='$|\psi_1(x)|^2$')
plot(x, (NPsi(x,psi[:,2]))**2, label='$|\psi_2(x)|^2$')
legend()
title('$|\psi_n(x)|^2$ - Normalizada')
xlabel('x')
ylabel('$|\psi_n(x)|^2$')
show()

"""
Como visto, a função de onda não estava normalizada. Para normalizar utilizei a definição do produto escalar no espaço de Hilbert.
"""
