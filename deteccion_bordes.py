import cv2

# Leer la imagen en escala de grises
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar el operador Sobel para detectar bordes en las direcciones x e y
sobelx = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=5)

'''
El operador Sobel es un operador de filtrado utilizado para calcular la aproximación de la
magnitud del gradiente de una imagen en cada píxel, resaltando los cambios abruptos de
intensidad que podrían corresponder a bordes en la imagen.'''

# Convertir las imágenes de salida a 8 bits
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)

# Combinar las imágenes de bordes en una sola imagen
bordes = cv2.addWeighted(sobelx, 0.1, sobely, 0.1, 0)

# Mostrar las imágenes
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Bordes', bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()