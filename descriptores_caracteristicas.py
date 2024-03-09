import cv2

'''
En resumen, los descriptores de características como SIFT y ORB son herramientas esenciales
en el campo de la visión por computadora para identificar y describir puntos de interés en imágenes,
lo que permite una amplia gama de aplicaciones prácticas.
'''
# Leer la imagen
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Inicializar los detectores de características
sift = cv2.SIFT_create()
orb = cv2.ORB_create()

# Detectar y describir características utilizando SIFT
keypoints_sift, descriptores_sift = sift.detectAndCompute(imagen, None)

# Detectar y describir características utilizando ORB
keypoints_orb, descriptores_orb = orb.detectAndCompute(imagen, None)

# Dibujar los keypoints en la imagen
imagen_sift = cv2.drawKeypoints(imagen, keypoints_sift, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
imagen_orb = cv2.drawKeypoints(imagen, keypoints_orb, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Mostrar las imágenes con los keypoints
cv2.imshow('SIFT', imagen_sift)
cv2.imshow('ORB', imagen_orb)
cv2.waitKey(0)
cv2.destroyAllWindows()