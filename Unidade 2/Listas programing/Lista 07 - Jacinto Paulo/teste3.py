def value(x):
    x = 1
def ref(x):
    x[0] = 1

x = 0
value(x) 
print("Valor: ", x) # o valor de x não foi alterado pela função.

x = [0]
ref(x)
print("Referência: ", x[0]) # o valor de x foi alterado pela função.
