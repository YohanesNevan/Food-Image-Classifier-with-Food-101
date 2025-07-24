# app.py
import streamlit as st
from PIL import Image
import requests
import os
import io
import json
from food_predictor import predict_food

st.title("🍽️ Food Image Classifier")
st.write("Upload gambar makanan dan dapatkan prediksi serta deskripsinya!")

uploaded_file = st.file_uploader("Upload gambar", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Baca gambar dari memory (bukan file path langsung)
    image_bytes = uploaded_file.read()
    img = Image.open(io.BytesIO(image_bytes))
    st.image(img, caption="Gambar yang diupload", use_column_width=True)

    os.makedirs("data", exist_ok=True)
    img_path = os.path.join("data", "temp.jpg")
    img.save(img_path)

    with st.spinner("Mendeteksi makanan..."):
        class_id, class_name, confidence = predict_food(img_path)

        # ✅ Tampilkan nama makanan besar di atas
        st.subheader("🍛 Nama Makanan")
        st.markdown(f"### **{class_name.capitalize()}**")
        st.write(f"🔍 Key class ID: `{class_id}`")
        st.write(f"📊 Akurasi prediksi: **{round(confidence * 100, 2)}%**")

        # ✅ Coba baca dari database lokal (jika ada)
        try:
            with open("data/food_db.json", "r", encoding="utf-8") as f:
                food_db = json.load(f)

            class_name_lower = class_name.lower()

            if class_name_lower in food_db:
                data = food_db[class_name_lower]

                st.subheader("📍 Asal Makanan")
                st.write(data["asal"])

                st.subheader("🧂 Bahan-bahan Umum")
                st.write(", ".join(data["bahan"]))

                st.subheader("📄 Deskripsi (Bahasa Indonesia)")
                st.write(data["deskripsi_id"])

            else:
                # Fallback ke Wikipedia jika tidak ditemukan
                st.subheader("📄 Deskripsi (Wikipedia Bahasa English)")
                wiki_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{class_name}"
                response = requests.get(wiki_url).json()
                if 'extract' in response:
                    st.write(response['extract'])
                else:
                    st.warning("Deskripsi tidak ditemukan 😕")

        except FileNotFoundError:
            st.error("Database lokal tidak ditemukan. Pastikan 'food_db.json' ada di folder 'data'.")