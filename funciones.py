# Definición de una función propia en Python
def saludar(nombre):
    """Función para saludar a una persona."""
    print("¡Hola,", nombre, "! ¿Cómo estás?")

# Llamada a la función con un argumento
saludar("Juan")

# Función con retorno de valor
def suma(a, b):
    """Función para sumar dos números."""
    resultado = a + b
    return resultado

# Llamada a la función y uso del valor retornado
resultado_suma = suma(5, 3)
print("El resultado de la suma es:", resultado_suma)

# Función con múltiples argumentos y valores predeterminados
def area_rectangulo(base=1, altura=1):
    """Función para calcular el área de un rectángulo."""
    area = base * altura
    return area

# Llamada a la función con valores predeterminados
area1 = area_rectangulo()  # base=1, altura=1 (valores predeterminados)
print("Área del rectángulo:", area1)

# Llamada a la función con argumentos específicos
area2 = area_rectangulo(3, 4)  # base=3, altura=4 (valores específicos)
print("Área del rectángulo:", area2)
