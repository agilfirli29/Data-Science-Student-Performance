# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institute

## Business Understanding
Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Mereka telah mencetak banyak lulusan dengan reputasi yang sangat baik, tetapi saat ini mereka menghadapi tantangan besar dalam mengatasi tingginya persentase mahasiswa yang melakukan *dropout* (putus kuliah). 

*Dropout* mahasiswa mengakibatkan kerugian dari dua sisi: bagi institusi, ini berarti kehilangan pendapatan dan berpotensi merusak reputasi. Bagi mahasiswa, ini dapat berdampak negatif pada masa depan karir dan finansial mereka. Oleh karena itu, Jaya Jaya Institut ingin mengidentifikasi mahasiswa yang berisiko *dropout* secepat mungkin agar bisa memberikan bimbingan khusus atau intervensi sedini mungkin.

## Permasalahan Bisnis
Permasalahan utama yang dipecahkan dalam proyek ini adalah tingginya angka *dropout* mahasiswa yang merugikan institusi dan mahasiswa itu sendiri. Institusi kesulitan untuk memetakan secara manual apa saja faktor-faktor utama pendorong terjadinya *dropout*, sehingga mereka membutuhkan sebuah sistem peringatan dini (*early warning system*) yang dapat memprediksi risiko tersebut secara otomatis.

## Cakupan Proyek
Untuk menyelesaikan permasalahan bisnis di atas, cakupan pengerjaan proyek ini meliputi:

1. **Analisis Data:** Melakukan tahapan Tanalisis data akan melibatkan pengumpulan, pemrosesan, dan eksplorasi data untuk mengidentifikasi pola dan tren yang relevan.
2. **Business Dashboard:** Membangun dashboard interaktif menggunakan **Looker Studio** untuk memantau metrik utama mahasiswa (demografi, akademik, finansial) secara *real-time*.
3. **Machine Learning:** Mengembangkan model prediktif menggunakan algoritma *Gradient Boosting* yang di-deploy melalui **Streamlit** untuk memprediksi status risiko mahasiswa di masa depan.

## Persiapan 
Sumber data: [data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
Pastikan Anda telah menginstal Python di komputer Anda. Proyek ini dikembangkan menggunakan Python versi 3.13. Berikut adalah panduan langkah demi langkah untuk menyiapkan environment dan menjalankan proyek secara lokal:

# Membuat Virtual Environment:
Buka Terminal atau Command Prompt, arahkan ke dalam direktori proyek (folder yang berisi file prediction.py dan requirements.txt), lalu jalankan perintah berikut:
`python -m venv env`

# Mengaktifkan Virtual Environment:
* Untuk pengguna Windows:
`env\Scripts\activate`
* Untuk pengguna Mac/Linux:
`source env/bin/activate`

# Menginstal Dependencies:
Setelah environment aktif, sangat disarankan untuk memperbarui pip terlebih dahulu, kemudian instal seluruh library yang dibutuhkan melalui file requirements.txt dengan perintah berikut:
`python -m pip install --upgrade pip`
`pip install -r requirements.txt`

## Business Dashboard 
Dashboard Jaya Jaya Institute dirancang untuk memberikan gambaran komprehensif tentang status mahasiswa (Graduate, Enrolled, Dropout). Visualisasi ini mencakup analisis faktor akademik (pilihan program studi), faktor finansial (status pembayaran UKT dan penerima beasiswa), serta demografi (jenis kelamin dan kategori usia).
Melalui dashboard ini, pihak manajemen kampus dapat memantau metrik utama seperti persentase dropout (32.1%) dan tingkat ketepatan pembayaran UKT secara real-time untuk mengambil keputusan berbasis data (data-driven decision).
**Akses Dashboard Interaktif:** [Lihat Dashboard di Looker Studio](https://lookerstudio.google.com/reporting/6d942783-3997-48b7-9d7a-bfd632e02542/page/0e1tF/edit)

## Menjalankan Sistem Machine Learning
Sistem prediksi ini telah di-deploy ke **Streamlit Cloud** agar dapat diakses oleh pihak manajemen kampus kapan saja tanpa perlu melakukan instalasi teknis.

Aplikasi ini bekerja dengan cara:
1. **Input Data:** Pengguna memasukkan data demografi, sosial-ekonomi, dan data akademik mahasiswa melalui formulir di sidebar (bilah samping).
2. **Prediksi Real-time:** Setelah menekan tombol 'Predict', model Machine Learning (Gradient Boosting) akan mengolah data tersebut secara instan.
3. **Hasil Interpretasi:** Aplikasi akan menampilkan status prediksi (Graduate, Enrolled, atau Dropout) beserta tingkat probabilitas atau keyakinan model terhadap prediksi tersebut.

**Akses Aplikasi ML:** [Student Performance Predictor](https://data-science-student-performance-agilfirligunawan.streamlit.app/)


## Conclusion
1. Hasil eksplorasi data analysis (EDA) dan visualisasi pada business dashboard, tingkat dropout mahasiswa di Jaya Jaya Institute tergolong cukup tinggi yaitu sekitar 32,1% dari total mahasiswa. Faktor utama yang berkaitan dengan dropout didominasi oleh aspek akademik dan finansial. Dari sisi akademik, performa mahasiswa pada semester awal, terutama jumlah mata kuliah yang lulus (approved) dan nilai rata-rata (grade) pada semester pertama dan kedua, menjadi indikator paling kuat terhadap keberlanjutan studi. Dari sisi finansial, status pembayaran biaya kuliah menunjukkan pengaruh signifikan, di mana mahasiswa yang belum melunasi cenderung memiliki risiko dropout lebih tinggi. Selain itu, faktor seperti status beasiswa, usia saat mendaftar, serta kondisi sosial seperti status pernikahan juga turut berkontribusi dalam membedakan karakteristik mahasiswa yang berpotensi dropout.
   
2. Berdasarkan hasil pemodelan Machine Learning, algoritma Gradient Boosting terpilih sebagai model terbaik dengan performa yang sangat baik, yaitu Accuracy sebesar 92,87%, serta nilai Precision, Recall, dan F1-Score yang masing-masing berada di kisaran 93%. Hal ini menunjukkan bahwa model mampu mengklasifikasikan status mahasiswa secara akurat dan seimbang. Berdasarkan analisis feature importance, faktor yang paling berpengaruh dalam prediksi dropout adalah Curricular units 2nd sem (approved), Curricular units 2nd sem (grade), Curricular units 1st sem (grade), Curricular units 1st sem (approved), serta Tuition fees up to date. Temuan ini mengindikasikan bahwa performa akademik di awal masa studi dan kondisi finansial merupakan faktor kunci, sehingga intervensi dini seperti monitoring akademik dan dukungan finansial sangat penting untuk menekan angka dropout


## Rekomendasi Action Items :
1. Program Bantuan Keuangan: Menyediakan skema pembayaran yang fleksibel (opsi cicilan) atau bantuan finansial khusus bagi mahasiswa yang teridentifikasi memiliki status hutang namun memiliki potensi akademik baik.

2. Program Peningkatan Akademik (Early Warning): Memberikan bimbingan akademik intensif atau konseling di akhir Semester 1 bagi mahasiswa yang jumlah SKS lulusnya berada di bawah rata-rata.

3. Pelatihan Tenaga Pengajar: Melatih dosen wali untuk lebih proaktif mendeteksi tanda-tanda kesulitan belajar pada mahasiswa sejak dini berdasarkan profil risiko demografi dan ekonomi.

