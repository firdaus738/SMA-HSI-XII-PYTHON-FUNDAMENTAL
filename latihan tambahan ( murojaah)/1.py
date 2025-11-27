"""
Validasi Input dengan while

Buat program yang meminta pengguna memasukkan umur mereka. Program harus terus meminta input
selama pengguna memasukkan nilai yang tidak valid (bukan angka atau angka di luar rentang wajar, misal <
0 atau > 100). Gunakan while True loop, try-except untuk menangani ValueError, dan if untuk
mengecek rentang. Jika input sudah valid, cetak umur tersebut dan hentikan loop dengan break.
"""

while True:
    try:
        umur = int(input("Masukan umur anda : "))
        if 0 <= umur <= 100:
            print (F"Umur anda adalah {umur} tahun")
            break
        else:
            print("Umur harus valid dari 0-100 . COBA LAGI!!!")

    except ValueError:
        print("Input tidak valid . MASUKAN ANGKA !!!")
