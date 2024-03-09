import cv2
import matplotlib.pyplot as plt

# Cargar la imagen desde el archivo
imagen = cv2.imread('imagen.jpg')

# Mostrar la imagen utilizando OpenCV
cv2.imshow('Imagen', imagen)

# Esperar a que se presione una tecla y luego cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()
