class persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return str(self.nombre)

class cola:
    def __init__(self):
        self.items = []
    def encolar(self, x):
        self.items.append(x)
    def desencolar(self):
        if self.esta_vacia():
            raise ValueError("la cola esta vacia")
        return self.items.pop(0)
    def esta_vacia(self):
        return len(self.items) == 0
    def __str__(self):
        for i in self.items:
            print(i)
        return " "

colabanco = cola()    
persona1 = persona("pipe")
persona2 = persona("pablo")
persona3 = persona("ariel")

colabanco.encolar(persona1)
colabanco.encolar(persona3)
colabanco.encolar(persona2)
print(colabanco)
colabanco.desencolar()
print(colabanco)
