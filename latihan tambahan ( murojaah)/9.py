"""Menghitung Mundur dengan Melewati Angka

Gunakan for loop dengan range() untuk menghitung mundur dari 20 ke 1. Tapi, jika angka tersebut
adalah kelipatan 4, jangan cetak angka tersebut (gunakan continue).
Contoh Output (sebagian):
20 (dilewati)
19
18
17
16 (dilewati)
15
..."""

for q in range(20,0, -1):
    if q % 4 == 0 :
        continue

    print(q)
