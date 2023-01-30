from numpy import array
from numpy.linalg import eigh

A = array([ [1,4,8,4],[4,2,3,7],[8,3,6,9],[4,7,9,2] ],float) 

a,V = eigh(A)
print (a)
print ('\n',V)


