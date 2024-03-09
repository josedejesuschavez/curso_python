import cv2

# Leer la imagen
imagen = cv2.imread('imagen.jpg')

# Obtener las dimensiones de la imagen
alto, ancho, canales = imagen.shape

# Mostrar las dimensiones de la imagen
print("Dimensiones de la imagen:")
print("Alto:", alto)
print("Ancho:", ancho)
print("Canales:", canales)

# Acceder y modificar un píxel específico
imagen[83, 135] = [255, 255, 255]  # Cambiar el píxel en la posición (100, 100) a blanco (255, 255, 255)

# Mostrar el valor del píxel modificado
print("\nValor del píxel modificado en (100, 100):", imagen[100, 100])

# Definir una región de interés (ROI) Region of Interest
roi = imagen[200:300, 300:400]  # Seleccionar la región de la imagen desde (200, 300) hasta (300, 400)

# Mostrar la ROI (Region of Interest)
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Modificar la ROI (hacerla roja)
roi[:] = [0, 0, 255]  # Establecer todos los píxeles en la ROI a rojo (0, 0, 255)

# Mostrar la imagen modificada con la ROI
cv2.imshow('Imagen con ROI modificada', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()