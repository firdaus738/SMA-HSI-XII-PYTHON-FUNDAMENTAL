""" Simulasi Password Lockout

Buat program login sederhana yang akan "mengunci" setelah 3 kali gagal.
-. Buat variabel password_benar = "rahasia123" dan maks_percobaan = 3.
/. Gunakan for loop dengan range(maks_percobaan).
0. Di dalam loop, minta pengguna memasukkan password.
1. Jika password benar, cetak "Login berhasil!" dan gunakan break untuk keluar dari loop.
3. Jika salah, cetak pesan yang menunjukkan sisa percobaan.
4. Gunakan else setelah for loop. Blok ini akan berjalan jika loop selesai tanpa break (artinya semua
percobaan gagal). Di dalamnya, cetak "Akun Anda terkunci!".
"""

password_benar = "aku firdaus"
maks_percobaan = 3

for percobaan in range (maks_percobaan):
    password = input ("masukin password nya :")

    if password == password_benar:
        print ("anda berhasil masuk !")
        break
    else:
        sisa = maks_percobaan - (percobaan + 1)
        if sisa > 0:
            print(f"password salah !!! sisa percobaan {sisa}")
        else:
            print("percobaan anda habis")

else:
    print ("akun anda kami tahan untuk sementara !!!!")