# Thomas Bar - 15 de Fevereiro de 2019

import numpy as np
import matplotlib.pyplot as plt

dados = np.loadtxt("thomascervejas.txt", int) #cerveja coluna 0 e tempo coluna 1
cervejas = dados[:, 0]
tempo = dados[:, 1]

plt.plot(tempo, cervejas)
plt.xlabel("Tempo (min)")
plt.ylabel("Cervejas (1uni - 600mL)")
plt.title("Thomas Bar")
plt.show()
