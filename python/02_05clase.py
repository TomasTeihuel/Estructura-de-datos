import random 

filas = int(input("ingrese la cantidad de filas de las matrices: "))
columnas = int(input("ingrese la cantidad de columnas de las matrices: "))

filas2 = int(input("ingrese la cantidad de filas de las matrices 2: "))
columnas2 = int(input("ingrese la cantidad de columnas de las matrices 2: "))

matriz1 = [[random.randrange(1, 3) for j in range(columnas)] for i in range(filas)]
matriz2 = [[random.randrange(1, 3) for j in range(columnas2)] for i in range(filas2)]

print("matriz 1:")
for fila in matriz1:
    print(fila)

print("matriz 2:")
for fila in matriz2:
    print(fila)

def multiplicacion(matriz1, matriz2):
    if columnas == filas2:
        for i in range(filas):
            for j in range(columnas):
                for k in range(len(matriz2)):
                    resultado[i][j] += matriz1[i][j] * matriz2[i][j]
                    return resultado 
    elif columnas != filas2:
        print("no se puede multiplicar, las columnas de la 1° matriz debe ser igual a la fila de la 2° matriz")
        return None

resultado = multiplicacion(matriz1, matriz2)
if resultado is not None:
    print("Resultado:")
