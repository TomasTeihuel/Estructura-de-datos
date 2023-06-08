import random
fila = 3
columna = 3
matriz_1 = [[random.randrange(-10, -5)for j in range(columna)]for j in range(fila)]

matriz_2 = [[random.randrange(-10, -5)for j in range(columna)]for j in range(fila)]


def mul(matriz_1, matriz_2):
    if len(matriz_1[0]) != len(matriz_2):
        return None
    
    fila = len(matriz_1)
    columna =len(matriz_1[0])
    columna =len(matriz_2[0])

    matriz_resultado = [[0 for j in range(columna)] for j in range(fila)]

    for i in range(fila):
        for j in range(columna):
            for k in range(columna):
                matriz_resultado[i][j] = matriz_1[i][j] * matriz_2[i][j]

    return matriz_resultado

print("matriz1:")
for (fila) in matriz_1:
    print(fila)

print("matriz1:")
for (fila) in matriz_2:
    print(fila)

print("matriz resultado de multiplicacion")
for (fila) in mul(matriz_1, matriz_2):
    print(fila)
