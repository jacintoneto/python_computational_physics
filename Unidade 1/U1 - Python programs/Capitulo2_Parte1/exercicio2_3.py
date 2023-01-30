from math import *

r = float(input("Informe o valor de r: "))
teta = float(input("Informe o valor de teta em graus: "))

rad = pi/180

x = r*cos(teta*rad)
y = r*sin(teta*rad)

print("O valor da posição x e y, respectivamente são: ", x, " e ", y)
