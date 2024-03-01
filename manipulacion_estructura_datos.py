# Acceso y manipulación de elementos en estructuras de datos en Python

# Lista de nombres
nombres = ["Ana", "Juan", "María", "Pedro", "Luisa"]

# Acceso a elementos por índice
print("Primer nombre:", nombres[0])
print("Último nombre:", nombres[-1])

# Manipulación de elementos
nombres[1] = "Carlos"     # Cambiar un nombre
nombres.append("Laura")   # Agregar un nombre al final
nombres.insert(2, "Sofía")# Insertar un nombre en una posición específica
nombres.remove("María")   # Eliminar un nombre por valor
nombres.pop()             # Eliminar el último nombre y devolverlo
del nombres[0]            # Eliminar un nombre por índice

# Imprimir lista después de manipulación
print("Lista de nombres después de manipulación:", nombres)

# Diccionario de información de personas
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceso a elementos por clave
print("Nombre de la persona:", persona["nombre"])
print("Edad de la persona:", persona["edad"])
print("Ciudad de la persona:", persona["ciudad"])

# Manipulación de elementos
persona["edad"] = 31       # Cambiar la edad de la persona
persona["profesion"] = "Ingeniero"  # Agregar una nueva clave y valor

# Imprimir diccionario después de manipulación
print("Información de la persona después de manipulación:", persona)
