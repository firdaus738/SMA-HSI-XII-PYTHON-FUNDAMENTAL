
#1
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blastoff!")


#2
angka_rahasia = 7

while True:
    try:
        tebakan = int(input("Tebak angka (1-10): "))
        if tebakan == angka_rahasia:
            print("Selamat, tebakan Anda benar!")
            break
        else:
            print("Salah, coba lagi!")
    except ValueError:
        print("Input tidak valid, masukkan angka.")
        
print("Terima kasih sudah bermain!")

#3
total = 0
count = 0

while True:
    angka = input("Masukkan angka (ketik 'done' untuk selesai): ")
    
    if angka.lower() == 'done':
        break
    
    try:
        angka_float = float(angka)
        total += angka_float
        count += 1
    except ValueError:
        print("Input tidak valid")
        continue

if count > 0:
    rata_rata = total / count
    print(f"Total: {total}")
    print(f"Jumlah angka: {count}")
    print(f"Rata-rata: {rata_rata}")
else:
    print("Tidak ada angka yang valid dimasukkan.")