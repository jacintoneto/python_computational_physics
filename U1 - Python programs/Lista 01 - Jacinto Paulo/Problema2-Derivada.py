# Desenvolvido por: Jacinto Paulo da Silva Neto
# Problema 2: Calculando derivadas

def f(x):
	return(x**2 - x)


# a) para delta = 10^{-2}
delta = 10**(-2)
print("\nA derivada de f(x) para delta igual a", delta, ".")
x = int(input("\nInforme valor de x: "))
df = (f(x+delta) - f(x))/delta
print("\n\nA derivada de f(x) no ponto x dado, para delta igual ", delta," é: ", df)

#Quando comparamos o resultado analítico para x=1, percebemos a divergência na 3ª casa após a vírgula. Elas não concordam perfeitamente devido ao fato de 10^{-2} não está tããão próximo de zero quanto é desejado para satisfazer a definição analítica.

#b) cálculo de f'(x) para valores de delta = 10^{-4} até 10^{-14}, passo 10^{-2}. Para simplificar o programa irei usar um laço.
print("\nAgora iremos computador o valor da derivada de f(x) para valores de deltas menos que 10^(-2).\n")
while(delta >= 10**(-14)):
	df = (f(x+delta) - f(x))/delta
	print("\nA derivada de f(x) no ponto x dado, para delta igual ", delta," é: ", df)
	delta=delta*(10**(-2))

#Era esperado que a medida que o delta diminuísse e, portanto, alcansasse cada vez mais o "valor absoluto" zero, a precisão da derivada numérica comparada com a analítia aumentasse. Contudo, devido a uma imprecisão do programa ao representar e computar diferenças com variáveis do tipo float, isso não ocorre. O resultado numérico começa a se distanciar do resultado analítico ainda quando delta é da ordem de 10^{-8}. Deve-se ter em mente que a definição númerica não satisfaz a definição analítica.
