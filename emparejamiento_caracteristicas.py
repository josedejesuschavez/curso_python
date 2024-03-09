import cv2
import numpy as np

# Leer las dos imágenes
imagen1 = cv2.imread('catedral4.jpeg', cv2.IMREAD_GRAYSCALE)
imagen2 = cv2.imread('catedral2.jpg', cv2.IMREAD_GRAYSCALE)

# Inicializar el detector de características SIFT
sift = cv2.SIFT_create()

# Encontrar y describir características en ambas imágenes
keypoints1, descriptores1 = sift.detectAndCompute(imagen1, None)
keypoints2, descriptores2 = sift.detectAndCompute(imagen2, None)

# Inicializar el algoritmo de coincidencia de fuerza bruta
bf = cv2.BFMatcher()

# Realizar el emparejamiento de características
matches = bf.knnMatch(descriptores1, descriptores2, k=2)

# Filtrar los mejores matches según el ratio de distancia
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

# Dibujar los matches en una imagen de salida
imagen_matches = cv2.drawMatches(imagen1, keypoints1, imagen2, keypoints2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Mostrar la imagen de salida
cv2.imshow('Emparejamiento de Caracteristicas', imagen_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()