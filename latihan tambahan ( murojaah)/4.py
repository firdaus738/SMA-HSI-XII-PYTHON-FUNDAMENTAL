"""
Mencari Bilangan Prima Pertama

Buat program untuk menemukan dan mencetak 5 bilangan prima pertama setelah angka 1. Bilangan prima
adalah bilangan yang hanya bisa dibagi oleh 1 dan dirinya sendiri.
Gunakan while loop luar untuk memastikan kamu sudah menemukan 5 bilangan prima.
Gunakan for loop di dalamnya untuk mengecek apakah sebuah angka bisa dibagi oleh angka lain
selain 1 dan dirinya sendiri.
Kamu akan butuh sebuah "flag" (variabel boolean) untuk menandai apakah sebuah angka prima atau
tidak.
"""

jumlah_prima = 0  # menghitung jumlah prima yg sudah di tentukan
angka = 2

while jumlah_prima < 100:
    is_prima = True


    for i in range(2,angka):
        if angka % i == 0:
         is_prima = False
        break
    if is_prima:
        print(angka,end=" ")
        jumlah_prima += 1

    angka += 1


    
        
