# Customer Support Ticket ETL Pipeline

## 📌 Deskripsi Proyek

Proyek ini merupakan implementasi **ETL (Extract, Transform, Load) Pipeline Automation** menggunakan dataset **Customer Support Ticket**. Proyek terdiri dari dua alur utama, yaitu **validasi kualitas data menggunakan Great Expectations** dan **otomasi ETL menggunakan PySpark, Apache Airflow, serta MongoDB Atlas**.

Pada alur pertama, dilakukan eksplorasi data, proses data cleaning, dan validasi kualitas data menggunakan Great Expectations. Hasil validasi disimpan dalam bentuk **Expectation Suite**, **Checkpoint**, dan **Data Docs** sebagai dokumentasi kualitas data.

Pada alur kedua, proses ETL diotomatisasi menggunakan **Apache Airflow**, dimana data diekstraksi dan ditransformasi menggunakan **PySpark**, kemudian hasil transformasi dimuat ke **MongoDB Atlas** sesuai jadwal yang telah ditentukan.

Proyek ini dibuat sebagai bagian dari assignment **Data Engineering** untuk memahami proses validasi data, pengolahan data menggunakan PySpark, serta workflow orchestration menggunakan Apache Airflow.

---

# 🎯 Tujuan

- Mengimplementasikan ETL Pipeline Automation menggunakan Apache Airflow.
- Melakukan validasi kualitas data menggunakan Great Expectations.
- Mengolah dan mentransformasi data menggunakan PySpark.
- Menyiapkan data agar siap disimpan ke MongoDB Atlas.
- Mengotomatisasi proses Extract, Transform, dan Load (ETL) sebagai implementasi workflow Data Engineering.

---

# 🔄 Alur Proyek

Proyek ini terdiri dari dua alur yang menggunakan dataset dan proses transformasi yang sama.

## 1. Data Validation menggunakan Great Expectations

### Extract
- Membaca dataset Customer Support Ticket menggunakan Pandas.
- Melakukan eksplorasi data sederhana untuk memahami struktur dan kondisi dataset.

### Transform
- Membersihkan data berdasarkan hasil eksplorasi.
- Menyesuaikan tipe data setiap kolom.
- Menangani missing values dan data yang tidak sesuai.
- Menyiapkan dataset sebelum dilakukan validasi.

### Data Validation
- Melakukan validasi kualitas data menggunakan Great Expectations.
- Menerapkan tujuh aturan validasi (Expectations).
- Menyimpan hasil validasi dalam bentuk:
  - Expectation Suite
  - Checkpoint
  - Data Docs

Pada alur ini **data tidak dimuat ke database**, melainkan hanya menghasilkan dokumentasi kualitas data.

---

## 2. ETL Automation menggunakan Apache Airflow

### Extract
- Membaca dataset menggunakan PySpark.
- Menghasilkan Spark DataFrame sebagai input proses transformasi.

### Transform
- Melakukan proses data cleaning menggunakan PySpark sesuai hasil eksplorasi sebelumnya.
- Menyesuaikan tipe data.
- Menangani missing values.
- Membersihkan data yang tidak konsisten.
- Menyiapkan dataset agar siap dimuat ke MongoDB.

### Load
- Menghubungkan aplikasi ke MongoDB Atlas menggunakan PyMongo.
- Mengubah hasil transformasi ke format yang sesuai.
- Menyimpan data ke collection MongoDB.

---

# ✅ Validasi Data (Great Expectations)

Proyek ini menerapkan **7 aturan validasi data** menggunakan Great Expectations.

1. Ticket ID harus unik.
2. Customer Age harus berada pada rentang 18–100 tahun.
3. Ticket Status hanya boleh berisi kategori yang valid.
4. Customer Age harus bertipe Integer.
5. Ticket ID tidak boleh bernilai Null.
6. Rata-rata Customer Age harus berada pada rentang yang ditentukan.
7. Date of Purchase harus menggunakan format YYYY-MM-DD.

Seluruh validasi berhasil dijalankan dan menghasilkan **Success = True**.

---

# ⏰ Workflow Automation

Workflow ETL diotomatisasi menggunakan **Apache Airflow** dengan tiga task utama:

1. Extract
2. Transform
3. Load

Workflow dijalankan secara otomatis menggunakan cron schedule berikut:

```python
schedule_interval = "10-30/10 9 * * 6"
```

Pipeline akan dijalankan setiap hari **Sabtu** pada pukul:

- 09:10
- 09:20
- 09:30

Pada setiap jadwal tersebut, pipeline akan membaca dataset, melakukan transformasi menggunakan PySpark, kemudian memuat data terbaru ke MongoDB Atlas.

---

# 🛠️ Tools & Library yang Digunakan

- Python
- Pandas
- PySpark
- Great Expectations
- Apache Airflow
- MongoDB Atlas
- PyMongo

---

# 📊 Dataset

Dataset yang digunakan adalah **Customer Support Ticket Dataset** yang berisi informasi mengenai tiket layanan pelanggan, profil pelanggan, prioritas tiket, status penyelesaian, produk yang dibeli, tanggal pembelian, serta informasi pendukung lainnya.

**Sumber Dataset:**

https://www.kaggle.com/datasets/muqaddasejaz/customer-support-ticket-dataset

---

# 📌 Hasil

Proyek ini berhasil mengimplementasikan dua alur utama dalam proses Data Engineering.

Pada alur pertama, dataset berhasil dibersihkan dan divalidasi menggunakan **Great Expectations**. Seluruh aturan validasi berhasil dipenuhi dan menghasilkan **Expectation Suite**, **Checkpoint**, serta **Data Docs** sebagai dokumentasi kualitas data.

Pada alur kedua, proses **ETL Pipeline** berhasil diotomatisasi menggunakan **Apache Airflow**. Data diekstraksi dan ditransformasi menggunakan **PySpark**, kemudian dimuat secara otomatis ke **MongoDB Atlas** sesuai jadwal yang telah ditentukan. Dengan demikian, data yang tersimpan di database selalu merupakan hasil transformasi terbaru dan siap digunakan untuk analisis maupun kebutuhan sistem selanjutnya.
