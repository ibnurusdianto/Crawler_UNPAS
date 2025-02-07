# Crawler Mahasiswa UNPAS

## Deskripsi
Program ini adalah crawler yang dirancang untuk mengunduh gambar mahasiswa dari situs web Universitas Pasundan berdasarkan rentang Nomor Induk Mahasiswa (NIM/NRP). Program ini menggunakan Python dan beberapa pustaka untuk menangani permintaan HTTP dan logging yang lebih baik.

## Fitur Utama
- **Pengunduhan Gambar**: Mengunduh gambar mahasiswa dari URL yang ditentukan.
- **Pengelolaan Direktori**: Membuat direktori untuk menyimpan gambar jika belum ada.
- **Logging yang Ditingkatkan**: Menggunakan `rich` untuk logging yang lebih informatif dan menarik.

## Ringkasan Peningkatan
### 1. Dukungan Emoji
- Menambahkan emoji untuk meningkatkan keterbacaan dan pengalaman pengguna dalam log dan output konsol.

### 2. Peningkatan Kinerja
- Memastikan pengunduhan gambar dilakukan secara efisien dengan streaming, serta meningkatkan logging untuk kejelasan.

### 3. Peningkatan Logika
- Menambahkan pemeriksaan dan log untuk memberi tahu pengguna tentang pembuatan direktori dan file yang sudah ada.

### 4. Peningkatan Fitur
- Meningkatkan antarmuka pengguna dengan seni ASCII dan instruksi yang lebih rinci.

### 5. Penanganan Kesalahan yang Ditingkatkan
- Memperbaiki pesan kesalahan untuk memberikan konteks dan panduan yang lebih baik kepada pengguna.

## Cara Menggunakan
1. Pastikan Anda memiliki Python dan pustaka yang diperlukan terinstal.
2. Jalankan program dan masukkan rentang ID yang diinginkan.
3. Gambar akan diunduh ke direktori `downloads`.

## Catatan
- Program ini mungkin mengalami masalah 403 Forbidden karena kontrol akses. Pastikan Anda memiliki izin yang diperlukan untuk mengakses gambar ini.


A configuration error or misconfiguration occurred because these images should be private or require authentication. The link https://situ2.unpas.ac.id/uploads/unpas/fotomhs/ should only be accessible after logging in, as accessing it should go through 'Student Data'. However, here, no login is required to access these images. If these images are indeed meant to be protected and accessible only by authenticated users, this is an example of Broken Access Control, as the server does not enforce authentication checks to access individual files.

![image](https://github.com/user-attachments/assets/e354365b-cd31-4652-996c-a0a0852684e3)
![Screenshot_2024-10-16_07_20_39](https://github.com/user-attachments/assets/3011a4bd-d6d7-4e4d-a227-6e06e742898b)

This program may not run because the website situ2.unpas.ac.id is currently experiencing a 403 Forbidden error. Please wait until the 403 Forbidden issue is resolved, and the program will run smoothly. Thank you.
