import cv2

# Leer la imagen en escala de grises
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar umbralización simple
# threshold = limite
umbral, imagen_umbralizada = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

# Mostrar las imágenes
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Umbralizada', imagen_umbralizada)
cv2.waitKey(0)
cv2.destroyAllWindows()