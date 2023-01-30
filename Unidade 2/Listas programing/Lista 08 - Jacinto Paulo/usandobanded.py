from banded import banded
import numpy as np

M = np.loadtxt("MatrixM.txt", float)
v = np.loadtxt("VetorT.txt", float)
up = 1; down = 1

x = banded(M,v,up,down)
print(x)
