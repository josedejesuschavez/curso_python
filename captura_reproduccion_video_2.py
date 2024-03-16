import cv2

# Abrir el archivo de video
cap = cv2.VideoCapture('example.mp4')  # 'video.mp4' es el nombre del archivo de video

# Comprobar si el archivo de video se ha abierto correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir el archivo de video.")
    exit()

# Leer y mostrar el video
while True:
    # Capturar un fotograma
    ret, frame = cap.read()

    # Verificar si el fotograma se ha capturado correctamente
    if not ret:
        print("Error: No se pudo capturar el fotograma.")
        break

    # Mostrar el fotograma
    cv2.imshow('Video', frame)

    # Esperar 30 milisegundos y comprobar si se ha presionado la tecla 'q' para salir del bucle
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar el archivo de video y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()