import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB7
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions
import numpy as np

# Cargar el modelo EfficientNetB7 preentrenado con pesos de ImageNet
model = EfficientNetB7(weights='imagenet')

# Leer una imagen de ejemplo
img_path = 'apple.jpg'
img = image.load_img(img_path, target_size=(600, 600))  # Tamaño de entrada recomendado para EfficientNetB7
x = image.img_to_array(img)
x = preprocess_input(x)
x = np.expand_dims(x, axis=0)

# Realizar la predicción utilizando el modelo
preds = model.predict(x)

# Decodificar las predicciones y mostrar las clases más probables
print('Predicciones:', decode_predictions(preds, top=30)[0])