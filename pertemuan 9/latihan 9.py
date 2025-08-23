"""Latihan 1: Ahli Indexing Diberikan string s = "Belajar Python itu Menyenangkan". Tulis kode untuk
mengambil dan mencetak:
-. Karakter pertama (B)
/. Karakter terakhir (n) menggunakan indexing negatif.
0. Karakter spasi pertama (di indeks 7).

Latihan 2: Master Slicing Masih menggunakan string s = "Belajar Python itu Menyenangkan".
Tulis kode slicing untuk mendapatkan dan mencetak substring berikut:
-. "Python"
Materi Pertemuan 9.md 2025-08-04
6 / 6
/. "Menyenangkan"
0. "Belajar"

Latihan 3: Membalik Kata Buatlah sebuah program yang:
-. Meminta pengguna memasukkan sebuah kata.
/. Menggunakan slicing untuk membalik kata tersebut.
0. Mencetak kata yang sudah dibalik.
1. Menggunakan if untuk mengecek apakah kata tersebut adalah palindrom (kata yang sama jika
dibaca dari depan maupun belakang, contoh: "kasur rusak"). Cetak pesan yang sesuai.

Latihan 4: Kode Rahasia Buatlah sebuah program yang mengambil "kode rahasia" dari sebuah kalimat
panjang. Aturannya adalah: ambil setiap karakter ketiga dari kalimat tersebut. Gunakan slicing dengan step
untuk mengekstrak dan mencetak kode rahasia dari kalimat:
"BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"

Latihan 5: Memperbaiki Nama Diberikan sebuah nama yang salah ketik: nama_salah = "dUDI
sANTOSO". Kamu belum belajar string methods seperti .title() atau .upper(). Gunakan hanya
indexing, slicing, dan penggabungan string (+) untuk memperbaiki nama tersebut menjadi "Budi
Santoso". Cetak hasilnya."""

#1

s = "Belajar Python itu Menyenangkan"

print("Karakter pertama:", s[0])  

print("Karakter terakhir:", s[-1]) 

print("Karakter spasi pertama:", s[7])  

#2
s = "Belajar Python itu Menyenangkan"

print(s[8:14])  

print(s[-12:])  

print(s[:7])  

#3
kata = input("Masukkan sebuah kata: ")
kata_terbalik = kata[::-1]

print("Kata setelah dibalik:", kata_terbalik)

if kata.lower() == kata_terbalik.lower():
    print("Kata tersebut adalah palindrom.")
else:
    print("Bukan palindrom.")

#4
kalimat ="BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"
kode_rahasia = kalimat[::2]  # ambil tiap 3 karakter
print("Kode Rahasia:", kode_rahasia)

#5
nama_salah = "dUDI sANTOSO"

# Ambil huruf pertama nama depan, ubah ke huruf besar
huruf_pertama = "B"
sisa_nama_depan = nama_salah[1:4].lower()  # 'udi'

huruf_pertama_belakang = "S"
sisa_nama_belakang = nama_salah[6:].lower()  # 'antoso'

# Gabungkan hasil
nama_benar = huruf_pertama + sisa_nama_depan + " " + huruf_pertama_belakang + sisa_nama_belakang
print("Nama yang benar:", nama_benar)