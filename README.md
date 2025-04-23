# Submission Pertama: Menyelesaikan Permasalahan Human Resources ✨

## Deskripsi
Submission proyek menyelesaikan permasalahan Human Resources (HR) ini adalah sebuah proyek pertama untuk penilaian praktik data science dari kelas Belajar Penerapan Data Science yang diberikan oleh Dicoding. Diharapkan dengan proyek ini dapat memberikan insight dan pemahaman mengenai data science.

## Struktur Proyek
- `meakhelg-dashboard`: File dashboard yang telah saya buat untuk submission kali ini.
- `meakhelg-dashboard`: Video penjelasan business dashboard yang telah dibuat dan kesimpulan dari dashboard tersebut.
- `metabase.db.mv.db`: File database dari Metabase.
- `model.pkl.`: File model Random Forest Classifier hasil modeling di notebook.ipynb.
- `notebook.ipynb`: File yang digunakan untuk melakukan Data Understanding, EDA, hingga Modeling, Evaluasi, dan Konklusi.
- `prediction.py`: File yang digunakan untuk menjalankan prediksi machine learning.
- `ulasan_gcal.csv`: File dataset hasil scraping dari aplikasi Google Calendar dari Play Store.
- `README.md`: File dokumentasi.

## Business Understanding
### Latar Belakang Masalah
Jaya Jaya Maju merupakan perusahaan multinasional dengan lebih dari 1000 karyawan. Namun, perusahaan mengalami permasalahan serius dalam manajemen SDM, khususnya tingginya angka attrition (keluar/mundurnya karyawan) yang mencapai lebih dari 10%.

Permasalahan Utama
Tingginya attrition rate dapat menyebabkan:
Hilangnya talenta berpengalaman,
Biaya tambahan untuk rekrutmen dan pelatihan karyawan baru,
Penurunan produktivitas tim.

Tujuan Proyek
Mengidentifikasi faktor-faktor apa saja yang paling memengaruhi keputusan karyawan untuk keluar dari perusahaan.
Memberikan insight yang dapat membantu departemen HR mengambil langkah preventif atau intervensi tepat sasaran.
Membangun business dashboard yang informatif untuk memonitor faktor-faktor terkait secara real-time dan mudah dipahami.


### Permasalahan Bisnis
Tuliskan seluruh permasalahan bisnis yang akan diselesaikan.

### Cakupan Proyek
Tuliskan cakupan proyek yang akan dikerjakan.

## Persiapan
### **Sumber Data**
Dataset yang digunakan dalam proyek ini adalah **[Dataset Karyawan Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)**, yang disediakan sesuai dengan instruksi pada submission proyek ini.

### **Menyiapkan Lingkungan (Environment Setup)**
Proyek ini memerlukan lingkungan yang sederhana untuk menjalankan **analisis data** dan **dashboard**. Berikut adalah langkah-langkah untuk mempersiapkan lingkungan kerja:

#### **1. Menjalankan Notebook.ipynb**
- Pastikan **dependensi**, **paket**, dan **library** yang dibutuhkan telah tersedia. Lihat **file `requirements.txt`** untuk mengetahui daftar dependensi yang diperlukan.
- Jalankan seluruh isi **notebook.ipynb** di **Google Colab** atau IDE sejenis untuk melihat hasil dari **analisis data**, temuan, dan **insight** yang diperoleh.

#### **2. Menjalankan Dashboard**
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


## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Conclusion
### Temuan Utama
- **OverTime (lembur)** adalah faktor paling signifikan: karyawan yang sering lembur jauh lebih berisiko untuk keluar.
- **MonthlyIncome** yang rendah, **usia muda**, dan **TotalWorkingYears** yang pendek juga meningkatkan kemungkinan attrition.
- Faktor lain seperti **YearsAtCompany**, **YearsInCurrentRole**, dan hubungan dengan manajer (**YearsWithCurrManager**) berpengaruh meskipun tidak dominan.

### Model Terbaik
Model **Random Forest** memberikan performa terbaik:
- Accuracy: **83.96%**
- Precision: **60%**
- Recall: **38.46%**
- F1-Score: **46.87%**
Model ini cukup unggul dalam mengenali karyawan yang *tidak keluar*, namun perlu peningkatan dalam mendeteksi yang *berisiko keluar*.

### Feature Importance (Top 5)
1. `OverTime_Yes` – 20.72%
2. `MonthlyIncome` – 11.61%
3. `Age` – 11.34%
4. `TotalWorkingYears` – 11.20%
5. `YearsAtCompany` – 9.47%

### Rekomendasi Action Items untuk Mengurangi Attrition dan Meningkatkan Retensi Karyawan:
1. **Kurangi Lembur yang Berlebihan**:  
   Karyawan yang sering lembur berisiko lebih tinggi untuk keluar. Perusahaan bisa menawarkan **waktu kerja fleksibel** atau **kerja jarak jauh** untuk membantu Work Life Balance.

2. **Tinjau Struktur Gaji**:  
   Gaji yang rendah sering kali meningkatkan attrition. Perusahaan perlu memastikan bahwa **struktur gaji** kompetitif dan menambah **insentif** atau **bonus** untuk meningkatkan kepuasan finansial.

3. **Optimalkan Beban Kerja dan Pengembangan Karir**:  
   Perusahaan perlu menyeimbangkan beban kerja dan menawarkan **peluang pengembangan** serta **promosi internal** untuk karyawan yang merasa stagnan.

4. **Implementasi Model Prediktif untuk Pemantauan**:  
   **Model Random Forest** dapat diintegrasikan ke dalam **dashboard HR** untuk memantau risiko attrition secara real-time dan memberi peringatan dini untuk tindakan proaktif.


### Kesimpulan
Dengan mengenali faktor-faktor kunci yang memengaruhi attrition, perusahaan dapat mengambil langkah strategis untuk meningkatkan **retensi karyawan**, menjaga keseimbangan kerja-hidup, dan menyesuaikan kebijakan kompensasi secara lebih tepat sasaran.
