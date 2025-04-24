# Submission Pertama: Menyelesaikan Permasalahan Human Resources ✨

## 📑 Deskripsi
Submission proyek menyelesaikan permasalahan Human Resources (HR) ini adalah sebuah proyek pertama untuk penilaian praktik data science dari kelas Belajar Penerapan Data Science yang diberikan oleh Dicoding. Diharapkan dengan proyek ini dapat memberikan insight dan pemahaman mengenai data science.

## 🗂 Struktur Proyek
- `dataset/` : Folder yang menyimpan semua dataset yang digunakan dalam proyek.
  - `data_bersih` : Berisi file CSV dari hasil proses cleaning.
  - `dataset_predict` : Berisi file CSV yang ingin di prediksi oleh model.
  - `fitur_penting` : Berisi file CSV berupa fitur-fitur penting yang memengaruhi Attrition.
  - `hasil_prediksi_model` : Berisi file CSV dari hasil proses prediksi model.
  - `hasil_prediksi_hr` : Berisi file CSV dari hasil proses prediksi model dari 'prediction.py'.
- `foto-dashboard/` : Folder yang menyimpan hasil konversi dashboard bentuk PDF ke JPG.
  - `meakhelg-dashboard-1.jpg` : Halaman pertama dashboard.
  - `meakhelg-dashboard-1.jpg` : Halaman kedua dashboard.
- `joblib_model.pkl`: File model Random Forest Classifier yang disimpan oleh joblib dari hasil modeling di notebook.ipynb.
- `meakhelg-dashboard`: File dashboard yang telah saya buat untuk submission kali ini.
- `meakhelg-video`: Video penjelasan business dashboard yang telah dibuat dan kesimpulan dari dashboard tersebut.
- `metabase.db.mv.db`: File database dari Metabase.
- `notebook.ipynb`: File yang digunakan untuk melakukan Data Understanding, EDA, hingga Modeling, Evaluasi, dan Konklusi.
- `pickle_model.pkl`: File model Random Forest Classifier yang disimpan oleh pickle dari hasil modeling di notebook.ipynb.
- `prediction.py`: File yang digunakan untuk menjalankan prediksi machine learning.
- `README.md`: File dokumentasi.

## 📌 Business Understanding
### 🎯 Latar Belakang
Perusahaan **Jaya Jaya Maju**, yang memiliki lebih dari 1.000 karyawan, tengah menghadapi tantangan serius di bidang manajemen sumber daya manusia, yaitu **tingginya tingkat attrition** atau keluarnya karyawan. Dengan angka attrition yang melebihi 10%, perusahaan mulai merasakan dampak langsung berupa hilangnya tenaga kerja berpengalaman menurunnya produktivitas organisasi, maupun permasalahan-permasalahan lainnya.

### ❗ Permasalahan Utama
Attrition yang tinggi bukan hanya berdampak pada efisiensi operasional, tetapi juga mencerminkan adanya potensi masalah struktural seperti:
- Ketidakpuasan saat di dunia kerja yang berimbas ke ketidakseimbangan kerja-hidup (work-life balance),
- Ketidakpuasan terhadap gaji, kompensasi, dan tunjangan, hingga adanya lembur dalam perusahaan,
- Ketidakharmonisan hubungan antar individu dan atasan, hingga lamanya bekerja dengan posisi dan/atau manager yang sama,
- Kurangnya jenjang karier yang jelas dan menarik dalam usia muda dan/atau status perkawinan.
Permasalahan ini harus direspons dengan pendekatan berbasis data agar solusi yang diterapkan benar-benar tepat sasaran.

### 🎯 Tujuan Proyek Permasalahan Bisnis
Proyek ini bertujuan untuk menyelesaikan permasalahan bisnis dengan:
1. **Mengidentifikasi faktor-faktor utama** yang memengaruhi keputusan karyawan untuk keluar dari perusahaan.
2. **Membangun model prediktif** berbasis machine learning untuk mengestimasi risiko keluar karyawan.
3. **Menyediakan business dashboard** yang dapat membantu tim HR dalam memantau kondisi tenaga kerja dan mengambil tindakan preventif secara lebih terukur.

### 📌 Cakupan Analisis
Analisis dilakukan terhadap beberapa aspek penting, antara lain:
- **Demografis**: seperti Usia, Gender, dan Status Pernikahan yang dapat memengaruhi komitmen kerja.
- **Kondisi kerja**: termasuk JobRole, Department, Business Travel, hingga Over Time.
- **Kompensasi**: seperti Monthly Income, Hourly Rate, Daily Rate, Stock Option Level, dan Percent Salary Hike.
- **Pengalaman dan kepuasan kerja**: seperti Years At Company, Years Since Last Promotion, Years With Current Manager, Job Satisfaction, Environment Satisfaction, hingga WorkLifeBalance.

### ⚙️ Strategi Analisis
- **Understanding and Exploratory Data Analysis**: melakukan pemahaman dan ekslorasi data dengan visualisasi untuk menelaah fitur-fitur yang berpotensi memiliki keterkaitan dengan Attrition.
- **Preprocessing Data**: melakukan perhitungan korelasi, encoding, penyeimbangan data dengan SMOTE, hingga melakukan feature selection. 
- **Pemodelan dan Evaluasi**: menggunakan berbagai algoritma (Logistic Regression, Random Forest, SVM, XGBoost, KNN) untuk menentukan model terbaik berdasarkan metrik seperti Accuracy, Precision, Recall, dan F1-Score.
- **Prediksi**: melakukan prediksi dengan model terbaik untuk mendeteksi karyawan yang berpotensi keluar.

## 🔧 Persiapan
### 💾 **Sumber Data**
Dataset yang digunakan dalam proyek ini adalah **[Dataset Karyawan Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)**, yang disediakan sesuai dengan instruksi pada submission proyek ini.

### 💻 **Menyiapkan Lingkungan (Environment Setup)**
Proyek ini memerlukan lingkungan yang sederhana untuk menjalankan **analisis data** dan **dashboard**. Berikut adalah langkah-langkah untuk mempersiapkan lingkungan kerja:

#### **1. Menjalankan notebook.ipynb**
- Pastikan **dependensi**, **paket**, dan **library** yang dibutuhkan telah tersedia. Lihat **file `requirements.txt`** untuk mengetahui daftar dependensi yang diperlukan.
- Jalankan seluruh isi **notebook.ipynb** di **Google Colab** atau IDE sejenis untuk melihat hasil dari **analisis data**, temuan, dan **insight** yang diperoleh.

#### **2. Menjalankan prediction.ipynb**
- Pastikan **dependensi**, **paket**, dan **library** yang dibutuhkan telah tersedia. Lihat **file `requirements.txt`** untuk mengetahui daftar dependensi yang diperlukan.
- prediction.py dapat dijalankan secara individu atau menggunakan **Google Colab** atau IDE sejenis dalam **notebook.ipynb** untuk menjalankan prediksi. Namun, saya menyarankan untuk menjalankannya menggunakan **Google Colab** atau IDE sejenis dalam **notebook.ipynb**.
- Pengguna hanya perlu mengganti pada
   ```bash
    predict_df = pd.read_csv('./dataset/dataset_predict.csv')  # Ganti path jika perlu
   ```
   untuk diganti ke path dengan dataset yang ingin di prediksi fitur Attrition-nya.
- Pengguna akan langusng mendapatkan hasil prediksi dalam bentuk .csv dengan nama 'hasil_prediksi_hr.csv' beserta dengan akurasi model untuk mendeteksi dataset.

#### **3. Menjalankan Dashboard**
Untuk melihat **dashboard** secara langsung, Anda dapat menggunakan **Metabase** dengan bantuan **Docker**. Pastikan **Docker** telah terpasang di sistem Anda.

**Langkah-langkah untuk menjalankan Metabase menggunakan Docker**:
1. **Tarik (pull) image Metabase dari Docker Hub** dengan perintah:
   ```bash
   docker pull metabase/metabase:latest
   ```

2. **Jalankan container Metabase** dengan perintah:
   ```bash
   docker run -p 3000:3000 --name metabase metabase/metabase
   ```

3. **Login ke Metabase** menggunakan kredensial berikut:
   - **Username**: `root@mail.com`
   - **Password**: `root123`

Dengan mengikuti langkah-langkah ini, Anda dapat memulai **analisis data** dan **dashboard**, serta melihat hasil visualisasi langsung di **Metabase**.

## 📊 Business Dashboard
### Ringkasan Dashboard  
Dashboard ini menganalisis data 1.058 karyawan untuk mengidentifikasi faktor penyebab tingginya attrition. Sebanyak 179 karyawan telah keluar, dan 40 lainnya diprediksi berisiko tinggi keluar oleh model.

### Faktor Utama Attrition  
Fitur paling berpengaruh adalah lembur (20.72%), yang diikuti pendapatan bulanan dan usia. Ini menandakan tekanan kerja dan kompensasi menjadi alasan dominan karyawan keluar.

### Distribusi dan Pola Karyawan Keluar  
- **Umur 25–35 tahun** paling banyak keluar.  
- **Laki-laki (58.6%)** mendominasi populasi.  
- **Status lajang (single)** memiliki attrition tertinggi.
- Adanya **lembur** membuat karyawan memiliki risiko untuk keluar.
- Karyawan dengan **gaji dibawah $5.000** juga lebih berisiko keluar.

### Job Role dan Risiko  
Bidang pekerjaan *Sales Representative* dan *Laboratory Technician* mencatat attrition tertinggi, sedangkan *Manager* dan *Research Director* relatif stabil.

### Tren Risiko  
Semakin tinggi usia, penghasilan, dan lama bekerja, maka semakin kecil kemungkinan karyawan keluar. Ini menunjukkan pentingnya retensi terhadap karyawan senior dan berpengalaman.

### Prediksi Model  
Model memprediksi 180 karyawan akan keluar, dengan probabilitas risiko individu ditampilkan dalam tabel (berada pada paling bawah dashboard). Karyawan dengan skor risiko tinggi perlu menjadi prioritas untuk intervensi HR.

## 🔍 Conclusion
### 🎯 Temuan Utama
- **OverTime (lembur)** adalah faktor paling signifikan: karyawan yang sering lembur jauh lebih berisiko untuk keluar.
- **MonthlyIncome** yang rendah, **usia muda**, dan **TotalWorkingYears** yang pendek juga meningkatkan kemungkinan attrition.
- Faktor lain seperti **YearsAtCompany**, **YearsInCurrentRole**, dan hubungan dengan manajer (**YearsWithCurrManager**) berpengaruh meskipun tidak dominan.

### 🤖 Model Terbaik
Model **Random Forest** memberikan performa terbaik:
- Accuracy: **83.96%**
- Precision: **60%**
- Recall: **38.46%**
- F1-Score: **46.87%**
Model ini cukup unggul dalam mengenali karyawan yang *tidak keluar*, namun perlu peningkatan dalam mendeteksi yang *berisiko keluar*.

### 🧠 Feature Importance (Top 5)
1. `OverTime_Yes` – 20.72%
2. `MonthlyIncome` – 11.61%
3. `Age` – 11.34%
4. `TotalWorkingYears` – 11.20%
5. `YearsAtCompany` – 9.47%

### ✍️ Rekomendasi Action Items untuk Mengurangi Attrition dan Meningkatkan Retensi Karyawan:
1. **Kurangi Lembur yang Berlebihan**:  
   Karyawan yang sering lembur berisiko lebih tinggi untuk keluar. Perusahaan bisa menawarkan **waktu kerja fleksibel** atau **kerja jarak jauh** untuk membantu Work Life Balance.

2. **Tinjau Struktur Gaji**:  
   Gaji yang rendah sering kali meningkatkan attrition. Perusahaan perlu memastikan bahwa **struktur gaji** kompetitif dan menambah **insentif** atau **bonus** untuk meningkatkan kepuasan finansial.

3. **Optimalkan Beban Kerja dan Pengembangan Karir**:  
   Perusahaan perlu menyeimbangkan beban kerja dan menawarkan **peluang pengembangan** serta **promosi internal** untuk karyawan yang merasa stagnan.

4. **Implementasi Model Prediktif untuk Pemantauan**:  
   **Model Random Forest** dapat diintegrasikan ke dalam **dashboard HR** untuk memantau risiko attrition secara real-time dan memberi peringatan dini untuk tindakan proaktif.


### ✅ Kesimpulan
Dengan mengenali faktor-faktor kunci yang memengaruhi attrition, perusahaan dapat mengambil langkah strategis untuk meningkatkan **retensi karyawan**, menjaga keseimbangan kerja-hidup, dan menyesuaikan kebijakan kompensasi secara lebih tepat sasaran.
