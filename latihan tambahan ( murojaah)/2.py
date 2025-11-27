"""
Pola Akumulator dengan while

Buat program untuk menghitung jumlah kuadrat dari N bilangan bulat pertama.
-. Minta pengguna memasukkan sebuah angka N.
/. Gunakan while loop untuk menghitung 1² + 2² + 3² + ... + N².
0. Cetak hasil akhirnya.
"""

N = int(input("Masukin bilangan bulat :"))
i = 1
total = 0

while i <= N:
    total += i**2
    i += 1

print(f"Jumlah kuadrat dari 1 sampe {N} adalah {total}")

