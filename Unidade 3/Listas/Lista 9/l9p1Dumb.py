# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 08:41:14 2019

@author: Jacinto Paulo
Professor: Leonardo Machado
Disciplina: Física Computacional I
Lista 9 - Problema 1
"""

import pylab as pl

def f(Vout, t, RC):
    if((int(2*t))%2 == 0): # Período deve ser T = 2pi
        Vin = 1
        return (Vin - Vout)/RC
   
    if( (int(2*t))%2 != 0):
        Vin = -1
        return (Vin - Vout)/RC

def RK4(Vout, t, RC):
    k1 = h*f(Vout, t, RC)
    k2 = h*f(Vout+k1/2, t+h/2, RC)
    k3 = h*f(Vout+k2/2, t+h/2, RC)
    k4 = h*f(Vout+k3, t+h, RC)
    
    return Vout + (1/6)*(k1+2*k2+2*k3+k4)

def intera(a, b, N, RC):
    listat = []
    listaVout = []
    h = (b-a)/N
    t = a
    Vout = Vout_0
    while(t < b):
        listat.append(t)
        listaVout.append(Vout)
        Vout = RK4(Vout, t, RC)
        t+=h
    return listat, listaVout, Vout

# Parâmetros e condições iniciais
a = 0
b = 5
Vout_0 = 0
N = 500
 
# Resolvendo EDO
## ------------------------------------------------------------------------------------ ##

listat = []
listaVout = []
h = (b-a)/N
t = a
Vout = Vout_0

RC = 1
while(t < b):
    listat.append(t)
    listaVout.append(Vout)
    Vout = RK4(Vout, t, RC)
    t+=h
    
pl.plot(listat, listaVout, color='c')
pl.title('Filtro Passa-Faixa - RC = 1')
pl.xlabel('$t$')
pl.ylabel('$V_{out}(t)$')
#pl.grid()
pl.clf
pl.show()


## ------------------------------------------------------------------------------------ ##
RC = 0.1
listat = []
listaVout = []
h = (b-a)/N
t = a
Vout = Vout_0

while(t < b):
    listat.append(t)
    listaVout.append(Vout)
    Vout = RK4(Vout, t, RC)
    t+=h
    
pl.plot(listat, listaVout, color='orange')
pl.title('Filtro Passa-Faixa - RC = 0.1')
pl.xlabel('$t$')
pl.ylabel('$V_{out}(t)$')
#pl.grid()
pl.show()
pl.clf()

## ------------------------------------------------------------------------------------ ##
RC = 0.01
listat = []
listaVout = []
h = (b-a)/N
t = a
Vout = Vout_0

while(t < b):
    listat.append(t)
    listaVout.append(Vout)
    Vout = RK4(Vout, t, RC)
    t+=h
    
pl.plot(listat, listaVout, color='purple')
pl.title('Filtro Passa-Faixa - RC = 0.01')
pl.xlabel('$t$')
pl.ylabel('$V_{out}(t)$')
#pl.grid()
pl.show()
pl.clf()

## -----------Todos------------------------------------------------------------------- ##

listat = []
listaVout = []
h = (b-a)/N
t = a
Vout = Vout_0

RC = 1
while(t < b):
    listat.append(t)
    listaVout.append(Vout)
    Vout = RK4(Vout, t, RC)
    t+=h
    
pl.plot(listat, listaVout, color='c', label='RC = 1')

RC = 0.1
listat = []
listaVout = []
h = (b-a)/N
t = a
Vout = Vout_0

while(t < b):
    listat.append(t)
    listaVout.append(Vout)
    Vout = RK4(Vout, t, RC)
    t+=h
    
pl.plot(listat, listaVout, color='orange', label = 'RC = 0.1')

## ------------------------------------------------------------------------------------ ##
RC = 0.01
listat = []
listaVout = []
h = (b-a)/N
t = a
Vout = Vout_0

while(t < b):
    listat.append(t)
    listaVout.append(Vout)
    Vout = RK4(Vout, t, RC)
    t+=h
    
pl.plot(listat, listaVout, color='purple', label='RC = 0.01')
pl.title('Filtro Passa-Faixa')
pl.legend()
pl.xlabel('$t$')
pl.ylabel('$V_{out}(t)$')
pl.show()

"""
O filtro passa-baixa é montado para permitir apenas a passagem de sinais abaixo da frequência de corte,
também conhecida nesse caso como frequência de potência w = 1/RC. O que podemos notar é que a cada meio período 
o sinal começa a ser cortado e a tensão descrece de forma brusca até atingir o mínimo no final do período.
Como podemos ver, quão maior for o valor de RC, menor será a frequência de potência e, portanto, menos frequências
serão permitidas. Quando diminuímos o valor da frequência uma faixa maior de frequência podem passar e o capacitor
vai conseguindo cada vez mais chegar ao carregamento total mais rápido e se manter lá por mais tempo (como em RC = 0.01). 
Porque quanto mais tempo o capacitor permanencer carregado, uma quantidade maior de sinais irá passar e serão medidos na 
saída.
"""