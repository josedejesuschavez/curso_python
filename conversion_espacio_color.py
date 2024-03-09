import cv2

# Leer la imagen en el espacio de color por defecto (BGR)
imagen = cv2.imread('imagen.jpg')

# Convertir la imagen a espacio de color RGB
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Convertir la imagen a espacio de color escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Mostrar las imágenes
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen RGB', imagen_rgb)
cv2.imshow('Imagen Escala de Grises', imagen_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()