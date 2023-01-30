from numpy import array,zeros
from time import monotonic
from pylab import plot, show

# Parâmetros do cálculo
N = 26
m,C,k,w = 1,1,6,2
alfa = -m*w**2+2*k

t1 = monotonic() 

# Vamos criar agora a matriz a ser resolvida
A = zeros([N,N],float)
v = zeros(N,float)
v[0] = C

for i in range(N):
    if (i == 0):
        A[i,i] = alfa - k
        A[i,i+1]= -k
    elif (i == (N-1)):
        A[i,i] = alfa -k
        A[i,i-1] = -k
    else:
        A[i,i] = alfa
        A[i,i-1] = -k
        A[i,i+1] = -k

#Algoritmo de Thomas
m = len(v) - 1
for i in range(m):
# Dividindo pelo elemento da diagonal
    p = A[i,i]
    A[i,i] = A[i,i]/p
    A[i,i+1]=A[i,i+1]/p
    v[i]=v[i]/p
# Zerando elementos abaixo da diagonal
    q = -A[i+1,i]
    A[i+1,i] = 0
    A[i+1,i+1] = A[i+1,i+1]+q*A[i,i+1]
    v[i+1]=v[i+1]+q*v[i]

v[m] = v[m]/A[m,m]
A[m,m] =1.0 
 
x = zeros(N,float)

x[m] = v[m]
#Substituição retrocedida
for i in range(m-1,-1,-1):
    x[i] = v[i] - A[i,i+1]*x[i+1]
    
t2 = monotonic()
print ("O tempo gasto foi", t2-t1)
plot(range(N),x)
plot(range(N),x,'ro')
show()
        
