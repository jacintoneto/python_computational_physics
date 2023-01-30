from numpy import exp, sqrt

def f(r):
    return V0*( (sigma/r)**6-exp(-r/sigma) )


V0 = 1.0
sigma = 1.0
acc = 1.0e-6
x1 = 1.0
x4 = 4.0
z = (1+sqrt(5))/2
x3 = x1 + (x4-x1)/z
x2 = x4 - x3 + x1

if ( f(x2) < f(x1) and f(x2) < f(x4) ) or  ( f(x3) < f(x1) and f(x3) < f(x4) ):
    while (abs(x4-x1)>acc):
        if f(x2) < f(x3):
            x4 = x3
            x3 = x2
            x2 = x4 - x3 + x1
        else:
            x1 = x2 
            x2 = x3
            x3 = x1 + (x4-x1)/z
    xmin = (x1+x4)/2.0
    print("O valor de r que minimiza o potencial de Buckingham é", xmin)
else:
    print("Não existe um mínimo no intervalo dado")
