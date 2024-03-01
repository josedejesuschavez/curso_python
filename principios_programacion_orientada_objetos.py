# Herencia, encapsulamiento y polimorfismo en Python

# Clase base (superclase)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        pass

# Subclase que hereda de Animal
class Perro(Animal):
    def sonido(self):
        return "Guau!"

# Subclase que hereda de Animal
class Gato(Animal):
    def sonido(self):
        return "Miau!"

# Subclase que hereda de Animal
class Vaca(Animal):
    def sonido(self):
        return "Muu!"

# Encapsulamiento y polimorfismo
def hacer_sonar_animal(animal):
    if isinstance(animal, Animal):
        print(animal.nombre + " hace " + animal.sonido())
    else:
        print("No es un animal válido.")

# Crear instancias de diferentes animales
perro = Perro("Bobby")
gato = Gato("Garfield")
vaca = Vaca("Betsy")

# Llamar a la función con diferentes instancias
hacer_sonar_animal(perro)  # Output: Bobby hace Guau!
hacer_sonar_animal(gato)   # Output: Garfield hace Miau!
hacer_sonar_animal(vaca)   # Output: Betsy hace Muu!
