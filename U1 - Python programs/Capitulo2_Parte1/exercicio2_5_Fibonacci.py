# Exercício 2.5 - Sequência de Fibonacci
# F(n) = F(n-1) + F(n-2) 
# def.: F(n)=x; F(n-1)=b; F(n-2)=a

n = int(input("Informe um valor limite para o último número que obece a distribuição de Fibonacci: "))
a,b,x=1,1,0 

while(x <= n):
	print(x)
	a = b
	b = x
	x = a + b
	



