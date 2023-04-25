import numpy as np

columna = int(input("ingrese cantidad de columnas: "))
fila = int(input("ingrese cantidad de filas: "))
matriz = np.zeros((fila, columna))

columna2 = int(input("ingrese cantidad de columnas: "))
fila2 = int(input("ingrese cantidad de filas: "))
matriz2 = np.zeros((fila2, columna2))

def matriz_1(fila, columna):
    for i in range(fila):
        for j in range(columna):
            matriz[i][j] += int(input(f"elemento:"))
    return print(matriz)

def matriz_2(fila2, columna2):
    for i in range(fila2):
        for j in range(columna2):
            matriz2[i][j] += int(input(f"elemento2:"))
    return  print(matriz2)

def suma(matriz, matriz2):
    rf = (matriz + matriz2), (matriz - matriz2)
    return rf
matriz_1(fila,columna)
matriz_2(fila2,columna2)
print("EL RESULTADO ES:", suma(matriz,matriz2))