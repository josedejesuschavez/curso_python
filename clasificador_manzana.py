import cv2
import numpy as np

# Leer la imagen de entrada
img = cv2.imread('apple.jpg')

# Convertir la imagen a espacio de color HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Definir el rango de colores de la manzana en HSV
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])

# Crear una máscara que detecte los píxeles en el rango de colores de la manzana
mask = cv2.inRange(hsv, lower_red, upper_red)

# Encontrar contornos en la máscara
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos alrededor de las regiones de color de la manzana
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100:  # filtro de área mínima
        cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)

# Mostrar la imagen con los contornos de la manzana
cv2.imshow('Apple Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()