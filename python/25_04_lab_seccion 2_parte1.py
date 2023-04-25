import random 

filas = int(input("ingrese la cantidad de filas de las matrices: "))
columnas = int(input("ingrese la cantidad de columnas de las matrices: "))

matriz1 = [[random.randrange(0, 5) for j in range(columnas)] for i in range(filas)]
matriz2 = [[random.randrange(0, 5) for j in range(columnas)] for i in range(filas)]
matriz3 = [[random.randrange(0, 5) for j in range(columnas)] for i in range(filas)]

print("matriz 1:")
for fila in matriz1:
    print(fila)

print("matriz 2:")
for fila in matriz2:
    print(fila)

print("matriz 3:")
for fila in matriz3:
    print(fila)

matriz_suma = []
for i in range(filas):
    fila_suma = []
    for j in range(columnas):
        suma = matriz1[i][j] + matriz2[i][j]
        fila_suma.append(suma)
    matriz_suma.append(fila_suma)

print("matriz suma:")
for fila in matriz_suma:
    print(fila)

matriz_resta = []
for i in range(filas):
    fila_resta = []
    for j in range(columnas):
        resta = matriz_suma[i][j] - matriz3[i][j]
        fila_resta.append(resta)
    matriz_resta.append(fila_resta)

print("matriz resta:")
for fila in matriz_resta:
    print(fila)