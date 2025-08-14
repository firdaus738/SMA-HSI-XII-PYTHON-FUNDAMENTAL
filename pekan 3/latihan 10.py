"""Latihan 1: Standarisasi Judul
Buat program yang meminta pengguna memasukkan judul buku yang mungkin diketik dengan huruf
besar/kecil yang acak (misal: "aLaDiN dan LaMPu aJAib"). Programmu harus membersihkan spasi ekstra di
awal/akhir dan mengubahnya ke format Title Case yang benar.


Latihan 2: Validasi Email Sederhana
Buat program yang meminta pengguna memasukkan alamat email. Program harus melakukan dua
pengecekan sederhana:
-. Apakah email mengandung karakter @? (Gunakan find() atau operator in).
/. Apakah email diakhiri dengan .com atau .co.id? (Gunakan .endswith()).
Cetak pesan "Email valid" atau "Email tidak valid" berdasarkan hasil pengecekan.


Latihan 3: Sensor Kata
Buat program yang memiliki sebuah kalimat dan sebuah kata yang ingin disensor. Program harus mengganti
semua kemunculan kata terlarang itu dengan tanda bintang ***.
Contoh: kalimat = "Harga tiketnya sangat mahal.", kata_sensor = "mahal".
Output yang diharapkan: "Harga tiketnya sangat ***."


Latihan 4: Akronim Generator
Buat program yang meminta pengguna memasukkan sebuah nama organisasi yang panjang (misal: "Badan
Usaha Milik Negara"). Program harus:
-. Memecah input menjadi list kata-kata.
/. Mengambil huruf pertama dari setiap kata.
0. Menggabungkan huruf-huruf pertama tersebut menjadi satu string akronim dalam huruf kapital.
Output yang diharapkan: "BUMN"


Latihan 5: URL Slug Generator
Di dunia web, "slug" adalah versi URL-friendly dari sebuah judul artikel. Buat program yang mengubah judul
artikel menjadi slug. Aturannya:
-. Ubah semua huruf menjadi kecil.
/. Ganti semua spasi dengan tanda hubung (-).
0. (Bonus) Hapus semua karakter selain huruf, angka, dan tanda hubung.
Contoh: judul = "10 Tips Jitu Belajar Python!"
Output yang diharapkan: "10-tips-jitu-belajar-python"""

#1
judul = input("Masukkan judul buku: ")
judul_bersih = judul.strip().title()
print("Judul standar:", judul_bersih)

#2
email = input("Masukkan email: ")

if "@" in email and (email.endswith(".com") or email.endswith(".co.id")):
    print("Email valid")
else:
    print("Email tidak valid")

#3
kalimat = "Harga tiketnya sangat mahal."
kata_sensor = "mahal"

kalimat_disensor = kalimat.replace(kata_sensor, "***")
print(kalimat_disensor)

#4
organisasi = input("Masukkan nama organisasi: ")

kata_kata = organisasi.split()
akronim = ""

for kata in kata_kata:
    akronim += kata[0].upper()

print("Akronim:", akronim)

#5
import re

judul_artikel = input("Masukkan judul artikel: ")
judul_lower = judul_artikel.lower()
judul_slug = re.sub(r'[^a-z0-9\s-]', '', judul_lower)  # hapus simbol
slug = "-".join(judul_slug.split())  # ganti spasi dengan '-'

print("Slug URL:", slug)
