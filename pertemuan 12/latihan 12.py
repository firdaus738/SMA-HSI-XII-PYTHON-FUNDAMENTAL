"""Latihan 1: Membuat Log Sederhana
Buat program yang berfungsi sebagai buku catatan (log).
-. Buka file bernama log_kegiatan.txt dalam mode append ('a').
/. Minta pengguna memasukkan sebuah kegiatan yang baru saja mereka lakukan.
0. Tulis input dari pengguna tersebut ke dalam file log_kegiatan.txt.
1. Pastikan setiap entri log berada di baris baru.
Jalankan program ini beberapa kali untuk menambahkan beberapa entri log.


Latihan 2: Salin File
Buat program yang menyalin isi dari satu file ke file lain.
-. Buat file sumber bernama sumber.txt dan isi dengan beberapa baris teks.
/. Program harus membuka sumber.txt dalam mode baca ('r').
0. Program harus membuka file tujuan bernama salinan.txt dalam mode tulis ('w').
1. Baca isi dari sumber.txt (bisa dengan .read() karena kita menyalin semuanya) dan tulis ke
salinan.txt.


Latihan 3: Hapus File dengan Aman
Buat program yang:
-. Meminta pengguna memasukkan nama file yang ingin dihapus.
/. Menggunakan os.path.exists() untuk mengecek apakah file tersebut benar-benar ada.
0. Jika ada, program harus meminta konfirmasi sekali lagi (misal: "Anda yakin ingin menghapus [nama
file]? (y/n)").
1. Jika pengguna mengetik 'y', gunakan os.remove() untuk menghapus file dan cetak pesan sukses.
3. Jika pengguna mengetik selain 'y' atau jika file tidak ada, cetak pesan yang sesuai"""

#1
with open("log_kegiatan.txt", "a") as file:
    kegiatan = input("Masukkan kegiatan yang baru saja dilakukan: ")
    file.write(kegiatan + "\n")

print("Kegiatan berhasil disimpan ke log_kegiatan.txt")

#2
sumber = "sumber.txt"
tujuan = "salinan.txt"

try:
    with open(sumber, "r") as file_sumber:
        isi = file_sumber.read()

    with open(tujuan, "w") as file_tujuan:
        file_tujuan.write(isi)

    print(f"Isi {sumber} berhasil disalin ke {tujuan}")
except FileNotFoundError:
    print(f"File {sumber} tidak ditemukan.")

#3
import os

nama_file = input("Masukkan nama file yang ingin dihapus: ")

if os.path.exists(nama_file):
    konfirmasi = input(f"Anda yakin ingin menghapus {nama_file}? (y/n): ").lower()
    if konfirmasi == "y":
        os.remove(nama_file)
        print(f"File {nama_file} berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
else:
    print("File tidak ditemukan.")

