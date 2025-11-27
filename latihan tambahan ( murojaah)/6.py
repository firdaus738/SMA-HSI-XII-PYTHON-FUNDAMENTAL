"""
Nested Loops untuk Pola Angka

Gunakan nested loops untuk menghasilkan pola angka berikut:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
Petunjuk: Loop luar mengontrol angka baris (1 sampai 5). Loop dalam mengontrol berapa kali angka
tersebut dicetak di baris itu.
"""

for q in range(1,6):
    for w in range(q):
      print(q, end=" ")
    print()