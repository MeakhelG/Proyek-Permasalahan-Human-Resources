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
Submission atau Proyek Pertama yang dilakukan ini bertujuan untuk memahami faktor-faktor yang memengaruhi tingkat attrition (keluar) karyawan di perusahaan Jaya Jaya Maju dan membangun model prediktif untuk mengidentifikasi karyawan dengan risiko keluar tinggi.

---
**1. Faktor-Faktor Penyebab Attrition**

Berdasarkan analisis data dan model prediktif, berikut adalah faktor utama yang memengaruhi **attrition** (keluar) karyawan di perusahaan Jaya Jaya Maju:

1. **OverTime**:  
   Karyawan yang sering lembur (**OverTime = Yes**) memiliki risiko keluar yang jauh lebih tinggi dibandingkan yang tidak lembur. Fitur ini adalah **prediktor terkuat** dalam model prediktif dan menunjukkan betapa pentingnya keseimbangan kerja-hidup dalam retensi karyawan.

2. **MonthlyIncome**:  
   Karyawan dengan **pendapatan bulanan lebih rendah** cenderung memiliki risiko keluar yang lebih tinggi. Hal ini menunjukkan bahwa **kepuasan finansial** adalah faktor penting dalam **retensi karyawan**. Gaji yang kompetitif dapat membantu perusahaan mengurangi tingkat attrition.

3. **Age**:  
   **Usia** karyawan juga mempengaruhi keputusan mereka untuk tetap atau keluar. Biasanya, karyawan dengan usia yang lebih muda atau yang berada di awal karier mereka lebih cenderung keluar jika mereka tidak merasa puas dengan kondisi kerja mereka.

4. **TotalWorkingYears**:  
   Karyawan dengan **masa kerja yang lebih pendek**, cenderung memiliki risiko keluar yang lebih tinggi. Mereka mungkin belum merasa cukup terikat dengan perusahaan atau belum menemukan kepuasan yang cukup dalam pekerjaan mereka.

5. **Fitur Pendukung Lain**:  
   - **YearsAtCompany**: Karyawan yang lebih lama bekerja di perusahaan memiliki risiko keluar yang lebih rendah, tetapi efeknya tidak sebesar faktor lainnya.
   - **YearsInCurrentRole**: Masa jabatan yang lebih lama di posisi saat ini juga berkontribusi pada risiko rendah keluar.
   - **YearsWithCurrManager**: Meskipun pengaruhnya kecil, hubungan dengan manajer juga berperan dalam keputusan karyawan untuk bertahan atau keluar.

---
**2. Model Prediktif Terbaik**
Model terbaik yang digunakan dalam proyek ini adalah **Random Forest**, dengan hasil evaluasi berikut:

- **Accuracy**: 83.96%
- **Precision**: 60%
- **Recall**: 38.46%
- **F1-Score**: 46.87%

Model **Random Forest** menunjukkan **performa yang lebih baik** dibandingkan model lain seperti **Logistic Regression**, **XGBoost**, **SVM**, dan **KNN**. Model ini menunjukkan **precision** yang cukup baik tetapi **recall** yang cukup rendah sehingga meskipun model efektif dalam mengidentifikasi karyawan yang tidak akan keluar, masih ada ruang untuk meningkatkan deteksi karyawan yang berisiko keluar.

---
**3. Feature Importance**
Berdasarkan analisis **feature importance** dari model **Random Forest**, berikut adalah faktor-faktor yang paling berpengaruh terhadap prediksi **attrition**:
- **OverTime_Yes**: Memiliki kontribusi terbesar dalam model dengan nilai **0.207205**.
- **MonthlyIncome**: Dengan kontribusi **0.116116**, gaji bulanan memainkan peran penting dalam keputusan karyawan untuk tetap atau keluar.
- **Age**: Usia memiliki kontribusi **0.113420** dalam memprediksi risiko keluar.
- **TotalWorkingYears**: Dengan kontribusi **0.112033**, masa kerja di perusahaan maupun di industri memengaruhi keputusan karyawan.
- **YearsAtCompany**: Memberikan kontribusi sebesar **0.094710**, menunjukkan bahwa lama bekerja di perusahaan dapat memengaruhi stabilitas karyawan.

**Feature Importance** lainnya juga memberikan wawasan mengenai elemen-elemen yang perlu dikelola dengan hati-hati, seperti **YearsInCurrentRole**, **StockOptionLevel**, dan **JobInvolvement**, yang meskipun memiliki kontribusi lebih kecil, tetap memiliki peran dalam keputusan attrition.

---
**Kesimpulan**:
Dengan memahami faktor-faktor utama yang mempengaruhi **attrition** karyawan dan menggunakan **model prediktif** yang efektif, perusahaan dapat **mengambil langkah-langkah proaktif** untuk mempertahankan karyawan dan mengurangi tingkat attrition. Rekomendasi ini, jika diterapkan dengan tepat, dapat membantu meningkatkan **kepuasan karyawan** dan mengurangi biaya perekrutan ulang.


### Rekomendasi Action Items untuk Mengurangi Attrition dan Meningkatkan Retensi Karyawan:
1. **Kurangi Lembur yang Berlebihan**:  
   Karyawan yang sering lembur berisiko lebih tinggi untuk keluar. Perusahaan bisa menawarkan **waktu kerja fleksibel** atau **kerja jarak jauh** untuk membantu Work Life Balance.

2. **Tinjau Struktur Gaji**:  
   Gaji yang rendah sering kali meningkatkan attrition. Perusahaan perlu memastikan bahwa **struktur gaji** kompetitif dan menambah **insentif** atau **bonus** untuk meningkatkan kepuasan finansial.

3. **Optimalkan Beban Kerja dan Pengembangan Karir**:  
   Perusahaan perlu menyeimbangkan beban kerja dan menawarkan **peluang pengembangan** serta **promosi internal** untuk karyawan yang merasa stagnan.

4. **Implementasi Model Prediktif untuk Pemantauan**:  
   **Model Random Forest** dapat diintegrasikan ke dalam **dashboard HR** untuk memantau risiko attrition secara real-time dan memberi peringatan dini untuk tindakan proaktif.
