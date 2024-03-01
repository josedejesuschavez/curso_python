# Manejo de errores con bloques try y except en Python

# Función que divide dos números
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None
    except TypeError:
        print("Error: Los operandos deben ser números.")
        return None


# Ejemplos de uso de la función dividir
print(dividir(10, 2))  # Imprime: 5.0
print(dividir(10, 0))  # Imprime un mensaje de error
print(dividir("10", 2))  # Imprime un mensaje de error
