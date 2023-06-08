import random
fila = int(input("ingresa cantidad de filas:"))
columna = int(input("ingrsa cantidad de columnas:"))

matriz1 = [[random.randrange(1, 5)for j in range(columna)] for i in range(fila)]
matriz2 = [[random.randrange(1, 5)for j in range(columna)] for i in range(fila)]

escalar = int(input("ingresa un numero para multiplicarlo por la matriz resultante, recuerda oucpar un numero entre el 1 y el 10 o no se tomara: "))
def pasa(escalar):
    if escalar < 1 or escalar > 10:
        return False
    else:
        return True
        

matriz_suma = []
for i in range(fila):
    fila_suma = []
    for j in range(columna):
        suma = matriz1[i][j] + matriz2[i][j]
        fila_suma.append(suma)
    matriz_suma.append(fila_suma)

matriz_resultado = [[elemento * escalar for elemento in fila]for fila in matriz_suma]

print("matriz1:")
for fila in matriz1:
    print(fila)

print("matriz2:")
for fila in matriz2:
    print(fila)

print("matriz suma:")
for fila in matriz_suma:
    print(fila)

print("matriz resultante:")
for fila in matriz_resultado:
    print(fila)