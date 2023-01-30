from numpy import array, empty

u = array([1, 2, 3], float)
v = empty(3, float) 

v = u

print("v = ", v, "\n\nu = ", u)


M = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], float)
print("\n\nM: \n", M)
w = empty(3, float)

# quando encontrar o valor que quer trocar
for i in range(3):  #esse método garante a troca efetiva das linhas
	w[i] = M[0,i]
	M[0,i] = M[1,i]
	M[1,i] = w[i]	
	

	

print("\n\nM: \n", M, "\n\n w = ", w)

