import cv2

# Inicializar el detector de objetos
tracker = cv2.TrackerCSRT_create()

# Capturar el primer fotograma
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
ret, frame = cap.read()

# Seleccionar una región de interés (ROI) para el objeto que se desea seguir
bbox = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)

# Inicializar el tracker con la ROI seleccionada
tracker.init(frame, bbox)

while True:
    # Capturar un fotograma
    ret, frame = cap.read()

    # Actualizar el tracker para seguir el objeto en el fotograma actual
    success, bbox = tracker.update(frame)

    # Dibujar el cuadro del objeto seguido en el fotograma
    if success:
        x, y, w, h = [int(i) for i in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Objeto perdido", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

    # Mostrar el fotograma con el seguimiento del objeto
    cv2.imshow("Frame", frame)

    # Esperar a que se presione la tecla 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar el dispositivo de captura de video y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
