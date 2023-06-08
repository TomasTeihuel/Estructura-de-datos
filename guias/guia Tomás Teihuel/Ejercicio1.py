matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

suma = [0,0,0,0,0]
for columna in matriz:
    for i in range(len(columna)):
        suma[i] += columna[i]
print(max(suma))

sumi = []
for fila in matriz:
    digref = sum(fila)
    sumi.append(digref)
print(min(sumi))