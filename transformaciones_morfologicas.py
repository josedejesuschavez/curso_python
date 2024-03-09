import cv2
import numpy as np

'''
Las operaciones morfológicas son un conjunto de técnicas utilizadas en procesamiento de imágenes
para manipular la forma o estructura de los objetos en una imagen. Estas operaciones se basan en
teoría matemática de morfología, que trata con la forma y estructura de los objetos.

Las operaciones morfológicas básicas más comunes son:

1. Erosión: Reduce el tamaño de los objetos en una imagen al eliminar píxeles en los bordes de los objetos.
Esto puede usarse para eliminar pequeños detalles o ruido, así como para separar objetos conectados.

2. Dilatación: Aumenta el tamaño de los objetos en una imagen al agregar píxeles a los bordes de los objetos.
Esto puede usarse para rellenar huecos en los objetos o para conectar objetos separados.
'''

# Leer la imagen en escala de grises
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar umbralización simple
_, imagen_umbralizada = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

# Definir el kernel para las operaciones morfológicas
kernel = np.ones((5,5), np.uint8)

# Aplicar erosión
imagen_erosionada = cv2.erode(imagen_umbralizada, kernel, iterations=1)

# Aplicar dilatación
imagen_dilatada = cv2.dilate(imagen_umbralizada, kernel, iterations=1)

# Mostrar las imágenes
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Umbralizada', imagen_umbralizada)
cv2.imshow('Imagen Erosionada', imagen_erosionada)
cv2.imshow('Imagen Dilatada', imagen_dilatada)
cv2.waitKey(0)
cv2.destroyAllWindows()