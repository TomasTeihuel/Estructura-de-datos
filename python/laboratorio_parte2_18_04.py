import random
columna = int(input("ingrese cantidad de columnas: "))
fila = int(input("ingrese cantidad de filas: "))

def matriz_1(fila, columna):
    m1 = []
    for i in range(fila):
        for j in range(columna):
            m1[i][j] = random.randint(1, 5)
            return m1

def matriz_2(fila, columna):
    m2 = []
    for i in range(fila):
        for j in range(columna):
            m2[i][j] =  (random.randint(1, 5)({i+1}, {j+1}))
            return m2
        
def suma(m1, m2):
    rf = (m1 + m2), (m1 - m2)
    return rf
print("EL RESULTADO ES:", suma())
suma()
