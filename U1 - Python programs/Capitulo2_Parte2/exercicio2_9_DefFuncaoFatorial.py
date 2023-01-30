#Exerc´ıcio 2.9: Fatorial

print("\n-----------------------------JACKSTARDUST-------------------------------")
print("\n\nEste algortimo calcula o fatorial de um número inteiro positivo n.")

def fatorial(n):
	f=1
	if (n==1):
		return 1
	else:
		for i in range(1,n+1,1):
			f = f*i
		return f

k = int(input("\n\nInforme n: "))

fat = fatorial(k)

print("\n\nO fatorial de ", k ," é, portanto: ", fat)
