import cv2
import numpy as np

# Cargar el modelo preentrenado
model_path = 'opencv_face_detector_uint8.pb'
config_path = 'opencv_face_detector.pbtxt'
net = cv2.dnn.readNetFromTensorflow(model_path, config_path)

# Inicializar la captura de video desde la cámara
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while True:
    # Leer un fotograma desde la cámara
    ret, frame = cap.read()

    # Preprocesar el fotograma (convertir a escala de grises y normalizar)
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), [104, 117, 123], False, False)

    # Pasar el fotograma preprocesado a través de la red neuronal
    net.setInput(blob)
    detections = net.forward()

    # Analizar las detecciones y dibujar los rectángulos de los rostros encontrados
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Umbral de confianza
            box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

    # Mostrar el fotograma con las detecciones de rostros
    cv2.imshow('Face Detection', frame)

    # Esperar a que se presione la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura de video y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()