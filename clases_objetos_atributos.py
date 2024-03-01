# Definición de la clase Persona
class Persona:
    # Método constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre   # Atributo nombre
        self.edad = edad       # Atributo edad

    # Método para mostrar información de la persona
    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

    # Método para incrementar la edad de la persona
    def cumpleanos(self):
        self.edad += 1
        print("Feliz cumpleaños! Ahora tienes", self.edad, "años.")

# Creación de objetos (instancias) de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Mostrar información de las personas
print("Información de la persona 1:")
persona1.mostrar_informacion()
print()

print("Información de la persona 2:")
persona2.mostrar_informacion()
print()

# Incrementar la edad de la persona 1
persona1.cumpleanos()

# Mostrar información actualizada de la persona 1
print("Información de la persona 1 después del cumpleaños:")
persona1.mostrar_informacion()
