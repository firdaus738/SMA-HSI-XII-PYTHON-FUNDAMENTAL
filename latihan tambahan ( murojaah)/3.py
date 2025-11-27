"""
Iterasi String dengan continue

Buat program yang meminta pengguna memasukkan sebuah kalimat. Program akan mencetak ulang kalimat
tersebut huruf per huruf, tetapi semua huruf vokal (a, i, u, e, o, baik besar maupun kecil) akan
dilewati (tidak dicetak).
"""

kalimat = input("Masukan kalimat :")
vokal = "aiueoAIUEO"

print("kalimat tanpa huruf vokal :")

for huruf in kalimat:
    if  huruf not in vokal:
        print(huruf,end="")

