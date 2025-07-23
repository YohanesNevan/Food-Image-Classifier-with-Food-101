.# Food-Image-Classifier-with-Food-101
Proyek deep learning untuk mengklasifikasikan gambar makanan ke dalam 101 kategori menggunakan dataset Food-101 dan model berbasis MobileNetV2.

---

# 🍱 Food Classifier using Food-101 Dataset

Proyek ini adalah sistem klasifikasi gambar makanan menggunakan dataset [Food-101](https://www.vision.ee.ethz.ch/datasets_extra/food-101/) dan model deep learning (MobileNetV2). Model ini mampu mengenali 101 jenis makanan dari seluruh dunia.

## 🧠 Fitur

* Deteksi otomatis gambar makanan dari kamera atau file
* Model CNN dengan MobileNetV2 + fine-tuning
* Dataset: Food-101 (75.000 gambar)
* Hasil pelatihan disimpan ke `food101_model_final.h5`
* Akurasi meningkat seiring jumlah epoch pelatihan

## 📁 Struktur Folder

```
food-Classifier-Project/
├── __pycache__/
│   └── food_predictor.cpython-312.pyc
├── data/
│   ├── food-101/
│   │   ├── images/
│   │   └── meta/
│   └── temp.jpg
├── saved_model/
│   ├── best_model.h5
│   └── food101_model_final.h5
├── app.py
├── food_predictor.py
├── requirements.txt
├── test_tf.py
└── train_model.py

```

## 🚀 Cara Menjalankan

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Jalankan pelatihan

```bash
python src/train.py
```

### 3. Jalankan Program

```bash
streamlit run app.py
```

Atau

```bash
python -m streamlit run app.py
```

## 🔧 Konfigurasi

* Epoch default: 10 (disarankan 30–100 untuk hasil lebih baik)
* Backbone: MobileNetV2 (dapat diganti dengan ResNet, EfficientNet, dll.)
* Ukuran gambar: 224x224

## ⚠️ Catatan

* Akurasi model tergantung jumlah epoch dan preprocessing dataset
* Jika laptop terlalu panas, gunakan epoch kecil dulu lalu lanjutkan

## 📷 Contoh Hasil

![contoh hasil](contoh_output.jpg)

## 🧑‍💻 Kontributor

* \[Yohanes Nevan] — Pelatihan model dan integrasi prediksi
* Dataset oleh ETH Zurich ([Food-101](https://www.vision.ee.ethz.ch/datasets_extra/food-101/))

---

