# Latihan 1: Fungsi Sapaan Sederhana Buatlah sebuah fungsi bernama salam_pembuka. Fungsi ini tidak
# memerlukan input (parameter). Ketika dipanggil, fungsi ini harus mencetak tiga baris teks:
# ==============================
# Selamat Datang di Program Saya!
# ==============================
# Panggil fungsi tersebut beberapa kali untuk melihat hasilnya.
def salam_pembuka():
    print("==============================")
    print("Selamat Datang di Program Saya!")
    print("==============================")

salam_pembuka()
salam_pembuka()


# Latihan 2: Fungsi dengan Parameter Buatlah sebuah fungsi bernama info_cuaca yang menerima dua
# parameter: kota dan cuaca. Ketika dipanggil (misal: info_cuaca("Jakarta", "berawan")), fungsi ini
# harus mencetak: Cuaca di kota Jakarta hari ini berawan.
def info_cuaca(kota, cuaca):
    print(f"Cuaca di kota {kota} hari ini {cuaca}.")

info_cuaca("Jakarta", "berawan")
info_cuaca("Bandung", "cerah")


# Latihan 3: Fungsi dengan return Buatlah sebuah fungsi bernama kubik yang menerima satu parameter
# numerik bernama angka. Fungsi ini tidak boleh mencetak apa-apa, sebaliknya ia harus mengembalikan
# hasil dari angka pangkat 3. Panggil fungsi ini dengan angka 4, simpan hasilnya dalam sebuah variabel
# bernama hasil_kubik, lalu cetak variabel tersebut.
def kubik(angka):
    return angka ** 3

hasil_kubik = kubik(4)
print("Hasil kubik dari 4 adalah:", hasil_kubik)



# Latihan 4: Kalkulator Diskon Buatlah sebuah program lengkap yang melakukan hal berikut:
# -. Buat sebuah fungsi bernama hitung_diskon yang menerima dua parameter: harga_awal dan
# persen_diskon.
# /. Di dalam fungsi, hitung jumlah diskon (harga_awal * (persen_diskon / 100)).
# 0. Di dalam fungsi, hitung harga akhir (harga_awal - jumlah_diskon).
# 1. Fungsi ini harus mengembalikan nilai harga_akhir.
# Materi Pertemuan 5.md 2025-07-28
# 8 / 8
# 3. Di luar fungsi, minta pengguna memasukkan harga barang dan persentase diskon. Jangan lupa
# konversi ke tipe data numerik.
# 4. Panggil fungsi hitung_diskon dengan input dari pengguna.
# 6. Tangkap hasil kembaliannya dan cetak harga akhir yang harus dibayar.
def hitung_diskon(harga_awal, persen_diskon):
    jumlah_diskon = harga_awal * (persen_diskon / 100)
    harga_akhir = harga_awal - jumlah_diskon
    return harga_akhir

# Input dari pengguna
harga = float(input("Masukkan harga barang: "))
diskon = float(input("Masukkan persen diskon: "))

# Hitung dan tampilkan
harga_setelah_diskon = hitung_diskon(harga, diskon)
print(f"Harga setelah diskon adalah: {harga_setelah_diskon}")


# Latihan 5: Konverter Suhu Buatlah sebuah fungsi fruitful bernama fahrenheit_ke_celsius yang
# menerima satu parameter: temp_f (temperatur dalam Fahrenheit). Fungsi ini harus menghitung dan
# mengembalikan temperatur dalam Celsius menggunakan rumus: (temp_f - 32) * 5/9. Panggil fungsi
# ini dengan nilai 98.6 dan cetak hasilnya
def fahrenheit_ke_celsius(temp_f):
    return (temp_f - 32) * 5 / 9

hasil_celsius = fahrenheit_ke_celsius(98.6)
print("98.6 Fahrenheit = ", hasil_celsius, "Celsius")