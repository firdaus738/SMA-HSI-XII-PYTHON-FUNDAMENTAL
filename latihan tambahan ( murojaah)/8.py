"""
Latihan 13: Membangun String dengan Pola

Buat program yang meminta input sebuah kata dari pengguna. Program kemudian harus membangun
sebuah string baru berbentuk "piramida" dari kata tersebut.
Gunakan for loop dengan range(len(kata)).
Gunakan slicing kata[:i+1] untuk mendapatkan potongan kata di setiap iterasi.
Contoh Input: "Python"
Contoh Output:
P
Py
Pyt
Pyth
Pytho
Python
"""

kata = input("masukan kata :")

for q in range(len(kata)):
    print(kata[:q + 2])
