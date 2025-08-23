"""Latihan 1: Tampilkan Semua Uppercase
Buat file puisi.txt. Tulis program yang:
-. Meminta pengguna memasukkan nama file (puisi.txt).
/. Membaca file tersebut baris per baris.
0. Mencetak setiap baris ke layar dalam format HURUF KAPITAL SEMUA.

Latihan 2: Hitung Rata-rata Spam Confidence
Gunakan file mbox-short.txt dari www.py4e.com/code3/mbox-short.txt.
Tulis program yang:
-. Membaca file baris per baris.
/. Mencari baris yang diawali dengan X-DSPAM-Confidence:.
0. Untuk setiap baris yang cocok, ekstrak angka desimal di akhir baris tersebut.
1. Hitung rata-rata dari semua angka yang berhasil diekstrak dan cetak hasilnya.
Petunjuk: Gunakan .startswith() dan slicing string. Konversi hasil slicing ke float.

Latihan 3: Easter Egg File
Modifikasi program Latihan 1. Jika pengguna memasukkan nama file yang persis sama dengan "na na
boo boo", program tidak boleh mencoba membuka file tersebut, melainkan harus mencetak pesan lucu:
NA NA BOO BOO TO YOU - You have been punk'd! dan kemudian berhenti. Untuk semua input
nama file lainnya, program harus berjalan normal (dan menangani FileNotFoundError jika file tidak ada)."""

#1
nama_file = input("Masukkan nama file: ")

try:
    # Membuka dan membaca file
    with open(nama_file, 'r') as file:
        for baris in file:
            print(baris.strip().upper())  # Cetak dalam huruf kapital semua
except FileNotFoundError:
    print("File tidak ditemukan.")

    
#2
nama_file = input("Masukkan nama file: ")

try:
    with open(nama_file, 'r') as file:
        total = 0
        jumlah = 0
        for baris in file:
            if baris.startswith("X-DSPAM-Confidence:"):
                angka = float(baris.strip().split(":")[1].strip())
                total += angka
                jumlah += 1
        if jumlah > 0:
            rata_rata = total / jumlah
            print("Rata-rata Spam Confidence:", rata_rata)
        else:
            print("Tidak ada baris X-DSPAM-Confidence ditemukan.")
except FileNotFoundError:
    print("File tidak ditemukan.")



#3
nama_file = input("Masukkan nama file 'na na boo boo' : ")

if nama_file.lower() == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(nama_file, 'r') as file:
            for baris in file:
                print(baris.strip().upper())
    except FileNotFoundError:
        print("File tidak ditemukan.")