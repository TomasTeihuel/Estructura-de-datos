import random

def crear_matriz():
    filas = random.randint(1, 3)
    columnas = random.randint(1, 3)
    
    matriz = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            elemento = int(input("Ingrese un elemento para la matriz: "))
            fila.append(elemento)
        matriz.append(fila)
    
    return matriz

matriz = crear_matriz()

print("Matriz generada:")
for fila in matriz:
    print(fila)