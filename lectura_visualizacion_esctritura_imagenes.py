import cv2
import matplotlib.pyplot as plt

# Lectura de la imagen
imagen = cv2.imread('imagen.jpg')

# Visualización de la imagen utilizando OpenCV
cv2.imshow('Imagen Original', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Escritura de la imagen en un nuevo archivo
cv2.imwrite('nueva_imagen.jpg', imagen)
print("La nueva imagen se ha guardado exitosamente.")