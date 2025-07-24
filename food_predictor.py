# food_predictor.py
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import json

# Load model yang telah kamu latih
model = load_model("saved_model/best_model.h5")

# Load class names (dari folder dataset Food-101)
class_indices = model.class_names if hasattr(model, 'class_names') else None

# Jika tidak tersedia, load dari folder
if class_indices is None:
    # Ambil nama folder (kelas) dari direktori data
    class_indices = sorted(os.listdir("data/food-101/images"))

def predict_food(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0  # Normalisasi

    preds = model.predict(x)
    class_id = np.argmax(preds)
    confidence = np.max(preds)
    class_name = class_indices[class_id]
    
    return class_id, class_name, confidence
