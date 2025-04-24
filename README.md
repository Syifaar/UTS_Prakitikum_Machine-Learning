## UTS Pemodelan Data - Klasifikasi Kredit Komputer

### 🧑‍💻 Nama: *Syifa Arifah Nurbayani*  
### 🆔 NIM: *1227050131*  
### 📁 Dataset: https://drive.google.com/file/d/1krLRWedghy_ysJ2N6i-1GJ-ZQUmnu6eu/view?usp=sharing

---

### 🔍 Deskripsi
Proyek ini bertujuan membuat model klasifikasi untuk menentukan apakah seseorang **layak mendapatkan kredit komputer** atau tidak berdasarkan atribut yang tersedia dalam dataset dummy.

---

## ✅ Tahapan Pembuatan Model

### 1. Import Library
Menggunakan pustaka Python seperti `pandas`, `scikit-learn`, dan `matplotlib` dll.

### 2. Load Dataset
Dataset dibaca menggunakan `pandas.read_csv()`. Data dieksplorasi awal seperti:
- `head()`, `info()`

### 3. Preprocessing
- Pisahkan **fitur (`X`)** dan **target (`y`)**
- Lakukan encoding untuk data kategorikal

### 4. Split Data
Data dibagi menjadi data latih dan data uji dengan rasio 80:20.

### 5. Model Decision Tree
Model dilatih menggunakan algoritma **Decision Tree Classifier** dari `sklearn` dan menggunakan pengaturan hyperparameter max_depth dengan nilai tetap 5.

### 6. Evaluasi Model
Model diuji menggunakan:
- **Akurasi**
- **Classification Report** (precision, recall, f1-score)
- **Confusion Matrix**

### 7. Visualisasi
Model divisualisasikan dalam bentuk **Decision Tree** agar mudah dianalisis.

---

## 📈 Hasil Evaluasi
Contoh metrik (diisi setelah dijalankan):
- Akurasi: 0.83

- Tidak Layak (0)
  
    - Precision (0): 0.78 — Ketika model memprediksi kelas 0 (misalnya, "Tidak     Layak"), 78% dari prediksi tersebut memang benar.

    - Recall (0): 0.73 — Dari semua contoh sebenarnya yang memiliki kelas 0,       model berhasil menemukan 73% dari mereka.

    - F1-Score (0): 0.75 — Ini adalah rata-rata harmonis dari precision dan recall, yang memberikan gambaran keseimbangan antara keduanya.

- Layak (1)
  - Precision (1): 0.86 — Ketika model memprediksi kelas 1 (misalnya, "Layak"), 86% dari prediksi tersebut memang benar.
  
  - Recall (1): 0.88 — Dari semua contoh sebenarnya yang memiliki kelas 1, model berhasil menemukan 88% dari mereka.
  
  - F1-Score (1): 0.87 — Sama seperti untuk kelas 0, f1-score ini memberikan gambaran keseimbangan antara precision dan recall untuk kelas 1.

---

## 🚀 Cara Menjalankan
1. Install Python dan dependensi.
2. Jalankan file `model.py` di terminal atau IDE:

```bash
python model.py
```

---

## 📂 Struktur Folder
```
UTS_Praktikum_Machine-Learning/
├── dataset_buys _comp.csv
├── model.py
└── README.md
```
