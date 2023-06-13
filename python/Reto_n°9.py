class libro:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return str(self.nombre)        

class libreria:
    def __init__(self):
        self.top = None
        self.libreria = []
    def push(self, libro):
        self.top = libro
        self.libreria.append(libro)
        return self.top
    def pop(self):
        if not self.is_emtpy():
            return self.libreria.pop()
        else:
            raise IndexError("la libreria esta vacia")
    def is_emtpy(self):
        return len(self.libreria) == 0
    def size(self):
        return len(self.libreria)
    def mostrar_libros(self):
        if self.libreria:
            print("Libros en la librería:")
            for libro in self.libreria:
                print(libro)
        else:
            print("La librería está vacía.")
    
libreria1 = libreria()
libro1 = libro("mi lucha")
libro2 = libro("condorito")
libro3 = libro("kama-sutra")

libreria1.push(libro1)
libreria1.push(libro2)
libreria1.push(libro3)
libreria1.mostrar_libros()
libreria1.pop()
libreria1.mostrar_libros()

