import cv2

# Abrir el dispositivo de captura de video (cámara)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 0 representa la cámara web predeterminada

# Verificar si la cámara se ha abierto correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

# Ciclo para capturar y mostrar el video
while True:
    # Capturar un fotograma desde la cámara
    ret, frame = cap.read()

    # Verificar si el fotograma se ha capturado correctamente
    if not ret:
        print("Error: No se pudo capturar el fotograma.")
        break

    # Mostrar el fotograma capturado en una ventana
    cv2.imshow('Video Capturado', frame)

    # Esperar a que se presione la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar el dispositivo de captura de video y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()