import cv2

# Leer la imagen
imagen = cv2.imread('imagen.jpg')

# Aplicar un filtro de suavizado (filtro de media)
imagen_suavizada = cv2.blur(imagen, (5, 5))  # Kernel de 5x5

# Mostrar las imágenes
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Suavizada', imagen_suavizada)
cv2.waitKey(0)
cv2.destroyAllWindows()