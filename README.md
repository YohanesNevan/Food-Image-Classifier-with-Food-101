# Food-Image-Classifier-with-Food-101
Proyek deep learning untuk mengklasifikasikan gambar makanan ke dalam 101 kategori menggunakan dataset Food-101 dan model berbasis MobileNetV2.

---

# 🍱 Food Recognition using Food-101 Dataset

Proyek ini adalah sistem klasifikasi gambar makanan menggunakan dataset [Food-101](https://www.vision.ee.ethz.ch/datasets_extra/food-101/) dan model deep learning (MobileNetV2). Model ini mampu mengenali 101 jenis makanan dari seluruh dunia.

## 🧠 Fitur

* Deteksi otomatis gambar makanan dari kamera atau file
* Model CNN dengan MobileNetV2 + fine-tuning
* Dataset: Food-101 (75.000 gambar)
* Hasil pelatihan disimpan ke `food101_model_final.h5`
* Akurasi meningkat seiring jumlah epoch pelatihan

## 📁 Struktur Folder

```
food-recognition/
├── dataset/
│   └── food-101/          # Dataset asli yang diekstrak dari food-101.tar.gz
├── model/
│   ├── food101_model_final.h5  # Model hasil pelatihan terakhir
│   └── best_model.h5           # Model dengan akurasi terbaik saat training
├── src/
│   ├── train.py           # Script untuk pelatihan model
│   └── predict.py         # Script untuk melakukan prediksi
├── requirements.txt
└── README.md
```

## 🚀 Cara Menjalankan

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Ekstrak dataset

Jika kamu sudah mengunduh `food-101.tar.gz`, ekstrak dengan:

```bash
tar -xvzf food-101.tar.gz
```

### 3. Jalankan pelatihan

```bash
python src/train.py
```

### 4. Prediksi makanan dari gambar

```bash
python src/predict.py --image path_ke_gambar.jpg
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

