# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:33:20 2019

@author: Luanna Karen
"""

#Disparo da bola de canhão

import numpy as np

m = 1.0; #kg
R = 0.08; #m
vo = 100; #m/s
rho = 1.22; #kg/m^3
C = 0.47;
g = 9.81; #m/s^2
k = np.pi*R**2*rho*C/(2*m);

def f(r,t):
    
    vx = r[2];
    vy = r[3];
    
    v = np.sqrt(vx**2 + vy**2);
    
    fx = vx;
    fy = vy;
    fvx = -k*vx*v
    fvy = -g -k*vy*v;
    return np.array([fx,fy,fvx,fvy],float);

def RK4(r,t,h):
    k1 = h*f(r,t);
    k2 = h*f(r + k1/2,t + h/2);
    k3 = h*f(r + k2/2,t + h/2);
    k4 = h*f(r + k3, t + h);
    return r + (k1 + 2*k2 + 2*k3 + k4)/6;

def NDsolve(ti,tf,theta,N): #Função que resolve a EDO
    
    vxi = vo*np.cos(theta); #m/s
    vyi = vo*np.sin(theta); #m/s
        
    h = (tf - ti)/N;
    t = ti;
    
    r = np.array([0,0,vxi,vyi]); #Partindo da origem
    
    while(True):

        r = RK4(r,t,h);
        t = t + h;
        if (r[1] < 0): #A condição de parada está na bola alcançar o chão (y = 0)
            break;
            
    return np.array([r[0],r[1]]);

def Function(ti,tf,theta,N,A):
    r = NDsolve(ti,tf,theta,N);
    return r[0] - A;
    
#Parâmetros iniciais
ti = 0.0; #s
tf = 20.0; #s
A = 200.0; #m Alcance desejado
tol = 0.1; #m Tolerância do cálculo

#Método da bissecção para encontrar o ângulo

theta1 = 45*np.pi/180;
theta2 = 80*np.pi/180;
theta = (theta1 + theta2)/2;

N = 10000; #Número de passos para a EDO

A1 = Function(ti,tf,theta1,N,A);
A2 = Function(ti,tf,theta2,N,A);
At = Function(ti,tf,theta,N,A);

while(abs(A2-A1) > tol):
    if (At*A1 > 0): 
        theta1 = theta;
        A1 = At;
    else:
        theta2 = theta;
        A2 = At;
        
    theta = (theta1 + theta2)/2;
    At = Function(ti,tf,theta,N,A);

r = NDsolve(ti,tf,theta,N);

print("\n * Ângulo certeiro:",theta*180/np.pi,"graus");  
print(" * Posição final:",r);  

erro = abs(r[0] - A)/A * 100;

print(" * Erro do cálculo:",erro,"%");