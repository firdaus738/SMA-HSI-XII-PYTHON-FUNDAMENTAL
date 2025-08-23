"""Latihan 1: Iterasi dan range() Gunakan for loop dan fungsi range() untuk mencetak semua bilangan
kelipatan 7 dari 0 hingga 70 (inklusif).
Latihan 2: Pola Akumulator dengan String Buat program yang memiliki sebuah string: kalimat =
"Python". Gunakan for loop untuk membangun string baru yang merupakan kebalikan dari string
tersebut.
Petunjuk: Inisialisasi string kosong kalimat_terbalik = "". Di dalam loop, tambahkan setiap
huruf ke depan kalimat_terbalik (kalimat_terbalik = huruf + kalimat_terbalik).
Output yang diharapkan: "nohtyP"
Latihan 3: Pola Pencarian (dengan if) Buat program yang menggunakan for loop dan range(1, 51)
untuk:
-. Memeriksa setiap angka dari 1 hingga 50.
/. Menghitung dan pada akhirnya mencetak berapa banyak angka yang habis dibagi 3 dan habis dibagi
5.
Petunjuk: Gunakan operator % dan and.
Latihan 4: Nested Loops untuk Pola Gunakan nested loops untuk membuat pola segitiga siku-siku terbalik
seperti di bawah ini:
*****
****
***
**
*
Materi Pertemuan 8.md 2025-07-31
7 / 7
Petunjuk: Loop luar for i in range(5, 0, -1) bisa membantu. Loop dalam akan mencetak *
sebanyak i kali.
Latihan 5: Faktorial Buat program yang meminta pengguna memasukkan sebuah bilangan bulat positif.
Program kemudian harus menghitung nilai faktorial dari angka tersebut menggunakan for loop. Faktorial
(n!) adalah hasil perkalian semua bilangan bulat positif dari 1 sampai n.
Contoh: Faktorial dari 5 (5!) adalah 5 * 4 * 3 * 2 * 1 = 120.
Petunjuk: Gunakan pola akumulator, tapi untuk perkalian. Inisialisasi hasil_faktorial = 1"""

#1
for i in range(0, 71, 7):
    print(i)

#2
kalimat = "Python"
kalimat_terbalik = ""

for huruf in kalimat:
    kalimat_terbalik = huruf + kalimat_terbalik

print(kalimat_terbalik)  

#3
jumlah = 0

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        jumlah += 1

print("Jumlah angka yang habis dibagi 3 dan 5:", jumlah)

#4
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

#5
n = int(input("Masukkan bilangan bulat positif: "))
hasil_faktorial = 1

for i in range(1, n + 1):
    hasil_faktorial *= i

print(f"Faktorial dari {n} adalah {hasil_faktorial}")
