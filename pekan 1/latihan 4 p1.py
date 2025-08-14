# Latihan 1: Program Perhitungan Upah dengan Lembur Buatlah sebuah program untuk menghitung total
# upah karyawan. Program harus meminta input jam kerja dan tarif per jam. Aturannya: jam kerja di atas 40
# jam dihitung sebagai waktu lembur dengan tarif 1.5 kali lipat dari tarif normal.
# Contoh Input: Jam = 45, Tarif = 10
# Perhitungan: (40 jam normal _ 10) + (5 jam lembur _ 10 * 1.5) = 400 + 75 = 475
# Contoh Output: Pay: 475.0

jam = float(input("Masukkan jumlah jam kerja: "))
tarif = float(input("Masukkan tarif per jam: "))

if jam > 40:
    lembur = jam - 40
    total = (40 * tarif) + (lembur * tarif * 1.5)
else:
    total = jam * tarif

print("Pay:", total)

#Latihan 2: Program Upah yang Aman dari Error Modifikasi program dari Latihan 1. Gunakan blok try dan
#except untuk menangani kasus di mana pengguna memasukkan teks (non-numerik) sebagai input jam
#atau tarif. Jika terjadi error, program harus menampilkan pesan Error, please enter numeric input
#dan berhenti dengan elegan tanpa crash.

try:
    jam = float(input("Masukkan jumlah jam kerja: "))
    tarif = float(input("Masukkan tarif per jam: "))
    
    if jam > 40:
        lembur = jam - 40
        total = (40 * tarif) + (lembur * tarif * 1.5)
    else:
        total = jam * tarif

    print("Pay:", total)

except:
    print("Error, please enter numeric input")


#    Latihan 3: Program Penilaian (Grading) yang Lengkap Buatlah sebuah program yang meminta input skor
#antara 0.0 dan 1.0.
#-. Gunakan try-except untuk menangani input non-numerik.
#/. Jika input numerik, periksa apakah skor berada dalam rentang 0.0 sampai 1.0. Jika tidak, tampilkan
#pesan error yang sesuai (misal: Bad score).
#0. Jika skor valid, tampilkan grade berdasarkan tabel berikut:
#>= 0.9 -> A
#>= 0.8 -> B
#>= 0.7 -> C
#>= 0.6 -> D
#< 0.6 -> F

try:
    skor = float(input("Masukkan skor (antara 0.0 sampai 1.0): "))

    if skor < 0.0 or skor > 1.0:
        print("Bad score")
    elif skor >= 0.9:
        print("Grade: A")
    elif skor >= 0.8:
        print("Grade: B")
    elif skor >= 0.7:
        print("Grade: C")
    elif skor >= 0.6:
        print("Grade: D")
    else:
        print("Grade: F")

except:
    print("masukan angka kocak")

#Latihan 4: Logika Pintu Masuk Wahana Buatlah sebuah program yang mensimulasikan aturan masuk ke
#sebuah wahana. Aturannya: "Pengunjung boleh masuk jika tingginya minimal 150 cm DAN (usianya di atas
#12 tahun ATAU didampingi orang tua)".
#-. Buat tiga variabel: tinggi_cm, usia, didampingi_ortu (berisi True atau False).
#/. Isi variabel-variabel tersebut dengan nilai apa pun untuk pengujian.
#0. Terapkan logika di atas menggunakan if dan operator and/or untuk mencetak "Boleh Masuk" atau
#"Tidak Boleh Masuk".
#1. Ubah-ubah nilai variabel untuk menguji semua kemungkinan skenario.


tinggi_cm = 145
usia = 13
didampingi_ortu = False

if tinggi_cm >= 150 and (usia > 12 or didampingi_ortu):
    print("Boleh Masuk")
else:
    print("Tidak Boleh Masuk")