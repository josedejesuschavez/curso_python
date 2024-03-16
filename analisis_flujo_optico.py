import cv2
import numpy as np

# Capturar el primer fotograma
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
ret, frame1 = cap.read()

# Convertir el primer fotograma a escala de grises
prvs_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

# Crear un cubo de color para dibujar los flujos ópticos
hsv = np.zeros_like(frame1)
hsv[..., 1] = 255

while True:
    # Capturar el siguiente fotograma
    ret, frame2 = cap.read()
    next_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Calcular el flujo óptico entre los dos fotogramas
    flow = cv2.calcOpticalFlowFarneback(prvs_gray, next_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Convertir el flujo óptico a coordenadas polares y cartesianas
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

    # Convertir el espacio de color HSV a BGR para visualización
    flow_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # Mostrar el flujo óptico en una ventana
    cv2.imshow('Optical Flow', flow_rgb)

    # Actualizar el fotograma anterior
    prvs_gray = next_gray

    # Esperar a que se presione la tecla 'q' para salir
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar el dispositivo de captura de video y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
