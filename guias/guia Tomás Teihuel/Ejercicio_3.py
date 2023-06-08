import numpy as np
matriz = np.random.randint(low=1, high=5, size=(3, 3))
print(matriz)
determinante = np.linalg.det(matriz)
print(determinante)