# Error Approximation Method using Trapezio

def f(x):
	return x**4 - 2*x + 1

def trapezio(a, b, N):
	h = (b-a)/N
	soma = 0.5*(f(b) + f(a))
	for k in range(1,N):
		soma += f(a + k*h)
	return h*soma

def R(i, m):
	if (m == 1):
		N = 2**(i-1)
		return trapezio(a, b, N)
	else:
		return RM[i, m-1] + (1.0/4.0**(m-1) - 1.0)*(RM[i, m-1] - RM[i-1, m-1])

