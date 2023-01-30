# Programa que calcula integrais usando a regra de Simpson

def f(x,y):
    return x**2*y**3

def w(k,N):
    if k==0 or k==N:
        return 1/3
    elif (k%2)==0:
        return 2/3
    else:
        return 4/3

def int2D(ax,bx,ay,by,Nx,Ny):
    hx = (bx-ax)/Nx
    hy = (by-ay)/Ny
    soma = 0.0
    for i in range(Nx+1):
        for j in range(Ny+1):
            soma += w(i,Nx)*w(j,Ny)*f(ax+i*hx,ay+j*hy)

    return hx*hy*soma

ax = 0.0
bx = 2.0
ay = 1.0
by = 5.0
Nx = 1000
Ny = 1000
integ = int2D(ax,bx,ay,by,Nx,Ny)

print("O valor estimado da integral é",integ,".")

