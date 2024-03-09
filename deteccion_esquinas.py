import cv2
import numpy as np

# Leer la imagen
imagen = cv2.imread('imagen.jpg')

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar el detector de esquinas Shi-Tomasi
esquinas = cv2.goodFeaturesToTrack(imagen_gris, maxCorners=100, qualityLevel=0.01, minDistance=10)

# Convertir las coordenadas de las esquinas a números enteros
esquinas = np.intp(esquinas)

# Dibujar los círculos alrededor de las esquinas detectadas
for esquina in esquinas:
    x, y = esquina.ravel()
    cv2.circle(imagen, (x, y), 3, (0, 255, 0), -1)

# Mostrar la imagen con las esquinas detectadas
cv2.imshow('Deteccion de Esquinas', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()