import random
print("Al ingresar filas y columnas esta se ocupara para ambas matrices")
columna = int(input("ingrese cantidad de columnas: "))
fila = int(input("ingrese cantidad de filas: "))

def matriz1(fila, columna):
    m1 = []
    for i in range(fila):
        for j in range(columna):
            m1[i][j] += random.randint(1, 5)
    return print(m1)

def matriz2(fila, columna):
    m2 = []
    for i in range(fila):
        for j in range(columna):
            m2[i][j] +=  random.randint(1, 5)
    return print(m2)
        
def suma(m1,m2):
    rf = m1 + m2
    return rf
matriz1(fila,columna)
matriz2(fila,columna)
print("el resultado es", suma(m1,m2))
