Berikut versi yang telah **diperbaiki dan dirapikan**, terutama pada bagian **link**, format markdown, dan konsistensi penulisan:

---

# 🍱 Food Classifier using Food-101 Dataset

Proyek deep learning untuk mengklasifikasikan gambar makanan ke dalam **101 kategori** menggunakan dataset [Food-101 dari ETH Zurich](https://www.vision.ee.ethz.ch/datasets_extra/food-101/) dan model berbasis **MobileNetV2**.

---

## 🧠 Fitur

* Deteksi otomatis gambar makanan dari kamera atau file
* Model CNN: **MobileNetV2** dengan fine-tuning
* Dataset: **Food-101** dengan 75.000 gambar (1000 gambar per kelas)
* Model hasil pelatihan disimpan sebagai `food101_model_final.h5`
* Akurasi meningkat seiring jumlah epoch pelatihan

---

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

---

## 🚀 Cara Menjalankan

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Unduh dan ekstrak dataset

Unduh dataset dari [Food-101 (ETH Zurich)](http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz), kemudian ekstrak:

```bash
tar -xvzf food-101.tar.gz
```

Letakkan folder hasil ekstrak (`food-101`) ke dalam folder `data/`.

### 3. Jalankan pelatihan

```bash
python train_model.py
```

### 4. Jalankan aplikasi klasifikasi

```bash
streamlit run app.py
```

Atau, alternatif lain:

```bash
python -m streamlit run app.py
```

---

## 🔧 Konfigurasi

* **Epoch** default: 10 (disarankan 30–100 untuk hasil lebih baik)
* **Backbone** model: MobileNetV2 (bisa diganti dengan ResNet, EfficientNet, dll.)
* **Ukuran gambar**: 224x224 px

---

## ⚠️ Catatan

* Akurasi model sangat dipengaruhi oleh jumlah epoch dan preprocessing
* Jika spesifikasi komputer rendah, gunakan epoch kecil terlebih dahulu

---

## 📷 Contoh Hasil

![Contoh output klasifikasi](contoh_output.jpg)

---

## 👨‍💻 Kontributor

* **Yohanes Nevan** — Pelatihan model dan integrasi prediksi
* Dataset oleh ETH Zurich — [Food-101](https://www.vision.ee.ethz.ch/datasets_extra/food-101/)

---

Kalau kamu ingin versi dalam bahasa Inggris atau ada tambahan seperti badge GitHub, lisensi, atau video demo, tinggal bilang saja!
