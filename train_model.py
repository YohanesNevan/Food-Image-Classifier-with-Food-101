# train_model.py
import os
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint

# Lokasi dataset
DATA_DIR = "data/food-101/images"
BATCH_SIZE = 32
IMG_SIZE = (224, 224)
EPOCHS = 1  # Ubah sesuai kebutuhan

# Generator untuk data training dan validasi
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

train_generator = train_datagen.flow_from_directory(
    DATA_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

val_generator = train_datagen.flow_from_directory(
    DATA_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# Bangun model dengan MobileNetV2
base_model = MobileNetV2(
    input_shape=IMG_SIZE + (3,),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False  # Freeze base model

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(101, activation='softmax')  # 101 kelas makanan
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 🔁 Cek apakah ada model sebelumnya
if os.path.exists("saved_model/best_model.h5"):
    print("🔁 Memuat bobot dari saved_model/best_model.h5")
    model.load_weights("saved_model/best_model.h5")
else:
    print("🆕 Tidak ada model sebelumnya, mulai training dari awal")


# 🔐 Checkpoint untuk menyimpan model terbaik
os.makedirs("saved_model", exist_ok=True)

checkpoint_cb = ModelCheckpoint(
    "saved_model/best_model.h5",
    save_best_only=True,
    monitor='val_accuracy',
    mode='max',
    verbose=1
)

# 🚀 Training
model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=EPOCHS,
    callbacks=[checkpoint_cb]
)

# Simpan model terakhir (meskipun belum tentu terbaik)
model.save("saved_model/food101_model_final.h5")
print("✅ Model akhir disimpan di saved_model/food101_model_final.h5")
print("✅ Model terbaik (berdasarkan val_accuracy) disimpan di saved_model/best_model.h5")
