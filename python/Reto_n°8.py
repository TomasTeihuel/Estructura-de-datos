estudiantes = {}

for i in range(3):
    nombre = input("Ingrese el nombre del estudiante: ")
    asignatura = input("ingrese asignatura: ")
    nota1 = float(input("ingrese nota del laboratorio 1: "))
    nota2 = float(input("ingrese nota del laboratorio 2: "))

    promedio = (nota1 * 0.3) + (nota2 * 0.7)

    estudiantes[nombre] = {
        "Asignatura" : asignatura,
        "Nota Laboratorio 1" : nota1,
        "Nota Laboratorio 2" : nota2,
        "Promedio Ponderado" : round(promedio,1)
    }
print("Información de los estudiantes:")
for estudiante, info in estudiantes.items():
    print(f"Estudiante: {estudiante}")
    print(f"Asignatura: {info['Asignatura']}")
    print(f"Nota Laboratorio 1: {info['Nota Laboratorio 1']}")
    print(f"Nota Laboratorio 2: {info['Nota Laboratorio 2']}")
    print(f"Promedio Ponderado: {info['Promedio Ponderado']}")
    print()