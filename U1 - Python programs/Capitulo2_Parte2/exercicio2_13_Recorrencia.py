#Exercıcio 2.13: Recorrencia

#até (n-1) pois meu i=1, assim, o primeiro termo, o "0", é deixado de fora, logo estou começando avançado na contagem, para isso devo compensar até onde meu n irá, assim como fiz.
print("\n Esse algotimo calcula o numero de catalão dado um número inteiro n.\n")
def catalan(n):
	C=1
	i=1
	if(n==0):
		return 1
	else:
		while(i <= n-1): 
			C = ((4*i-2)/(i+1))*C 
			i+=1
		return C

k = int(input("\nInforme até qual valor de n você quer obter o número de catalão: "))

catalao = catalan(k)
print("O numero catalão dado ", k, " é: ", catalao)
