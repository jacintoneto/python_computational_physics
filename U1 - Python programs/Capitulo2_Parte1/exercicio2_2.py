#Exercício 2.2
g = 9.81
h = float(input("Informe a altura inicial em metros: "))
t = float(input("Informe o tempo em segundos que se passou desde que você a lançou: "))

y = h - 0.5*g*t**2/2 

if(y >= 0):
	print("A altura atual da bola é no tempo", t,": ", y)
else:
	print("O corpo atravessou o chão... Está abaixo do solo à: ", y)
