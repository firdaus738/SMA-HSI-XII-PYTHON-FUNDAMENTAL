"""
Permainan "FizzBuzz"

Ini adalah soal wawancara coding klasik. Tulis program yang menggunakan for loop untuk mencetak angka
dari 1 hingga 100, dengan aturan:
Jika angka tersebut kelipatan 3, cetak "Fizz".
Jika angka tersebut kelipatan 5, cetak "Buzz".
Jika angka tersebut kelipatan 3 dan 5, cetak "FizzBuzz".
Jika tidak memenuhi ketiganya, cetak angka itu sendiri.
Contoh Output (sebagian):
1
2
Fizz
4
Buzz
Fizz
7
...
14
FizzBuzz
...
"""

for angka in range (1,50):
    if angka % 4 == 0 and angka % 8 == 0 :
        print ( "uuuuu")
        
    elif angka % 4 == 0:
        print("ooooo")
    elif angka % 9 == 0:
        print("iiiii")
    else:
        print(angka)