import random
fila = 3
columna = 3
matriz_1 = [[random.randrange(5, 10)for j in range(columna)]for j in range(fila)]

print("matriz1:")
for fila in matriz_1:
    print(fila)