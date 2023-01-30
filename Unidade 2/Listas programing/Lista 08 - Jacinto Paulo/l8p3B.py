"""
Desenvolvido por: Jacinto Paulo 
Disciplina: Física Computacional I
Professor: Leonardo 

Lista 8 - Problema 3 - Letras B

"""

from numpy import loadtxt, zeros, dot
from numpy.linalg import norm

N = 4 #dimensão da matriz
Q = zeros([N,N], float)
R = zeros([N,N], float)
A = loadtxt('MatrizA.txt', float)
U = zeros([N,N], float)

# Matriz Q
# Primeira coluna de U, coluna zero
U[:, 0] = A[:,0] # vetores: u0 = a0
Q[:,0] = U[:,0]/norm(U[:, 0]) 

# Para i > 0.
for m in range(1, N): #slicing funciona semelhante a uma terceira variável que seria quem corre na linhas com coluna fixa.
	U[:, m] = A[:, m]
	for j in range(m):
		U[:, m] -= dot(Q[:, j],A[:, m])*Q[:, j] # U = A a não ser por essa quantidade associada a Q e A.s
	Q[:, m] = U[:, m]/norm(U[:, m])

# Matriz R
# Os elementos de R são formados pelo produto das colunas de Q e A, sendo que em R a coluna de Q é a linha e de A a coluna.  
for i in range(N):
	for j in range(i,N): #diagonal superior
		R[i, j] = dot(Q[:, i], A[:, j]) 

print("A:\n", A, "\n\nQ:\n", Q, "\n\nR:\n", R)

# Produto QR = A
U = dot(Q,R)
print("\n\nA = dot(Q,R):\n", U)
