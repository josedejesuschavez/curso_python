# Estructuras de control en Python: condicionales y bucles

# Condicionales (if, elif, else)
numero = 10

if numero > 0:
    print("El número es positivo.")
elif numero == 0:
    print("El número es cero.")
else:
    print("El número es negativo.")

# Bucle for
lista = [1, 2, 3, 4, 5]

print("Elementos de la lista:")
for elemento in lista:
    print(elemento)

# Bucle while
contador = 0

print("Contando hasta 5:")
while contador < 5:
    print(contador)
    contador += 1
