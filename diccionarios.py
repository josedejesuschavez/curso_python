# Diccionarios y su uso en Python

# Crear un diccionario vacío
diccionario = {}

diccionario_data = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Madrid'
}

# Agregar pares clave-valor al diccionario
diccionario["nombre"] = "Juan"
diccionario["edad"] = 30
diccionario["ciudad"] = "Madrid"

# Imprimir el diccionario completo
print("Diccionario completo:", diccionario)
print("Diccionario completo pre iniciado:", diccionario_data)

# Acceder a un valor utilizando su clave
print("Nombre:", diccionario["nombre"])
print("Edad:", diccionario["edad"])
print("Ciudad:", diccionario["ciudad"])

# Modificar un valor existente
diccionario["edad"] = 35
print("Edad actualizada:", diccionario["edad"])

# Eliminar un par clave-valor del diccionario
del diccionario["ciudad"]
print("Diccionario después de eliminar la clave 'ciudad':", diccionario)

# Verificar si una clave existe en el diccionario
if "nombre" in diccionario:
    print("La clave 'nombre' existe en el diccionario.")
else:
    print("La clave 'nombre' no existe en el diccionario.")
