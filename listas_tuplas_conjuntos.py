# Listas, tuplas y conjuntos en Python

# Listas: colección ordenada y mutable de elementos
lista = [1, 2, 3, 4, 5]

# Acceder a elementos de la lista
print("Primer elemento de la lista:", lista[0])
print("Último elemento de la lista:", lista[-1])

# Modificar elementos de la lista
lista[0] = 10
print("Lista después de modificar el primer elemento:", lista)

# Añadir elementos a la lista
lista.append(6)
print("Lista después de añadir un nuevo elemento:", lista)

# Eliminar elementos de la lista
lista.remove(3)
print("Lista después de eliminar el elemento '3':", lista)

# Tuplas: colección ordenada e inmutable de elementos
tupla = (1, 2, 3, 4, 5)

# Acceder a elementos de la tupla
print("Primer elemento de la tupla:", tupla[0])
print("Último elemento de la tupla:", tupla[-1])

# Conjuntos: colección no ordenada y mutable de elementos únicos
conjunto = {1, 2, 3, 4, 5, 4000}
conjunto_set = set([1, 2, 3, 4, 5, 4000, 4000])

# Añadir elementos al conjunto
conjunto.add(6)
conjunto_set.add(6)
print("Conjunto después de añadir un nuevo elemento:", conjunto, conjunto_set)

# Eliminar elementos del conjunto
conjunto.remove(3)
print("Conjunto después de eliminar el elemento '3':", conjunto)
