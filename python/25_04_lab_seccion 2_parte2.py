import random 

filas = int(input("ingrese la cantidad de filas de las matrices: "))
columnas = int(input("ingrese la cantidad de columnas de las matrices: "))

matriz1 = [[random.randrange(0, 10) for j in range(columnas)] for i in range(filas)]

escalar = int(input("Ingrese el escalar a multiplicar: "))

print("matriz 1:")
for fila in matriz1:
    print(fila)

matriz_resultado = [[elemento * escalar for elemento in fila] for fila in matriz1]

print("matriz resultante:")
for fila in matriz_resultado:
    print(fila)