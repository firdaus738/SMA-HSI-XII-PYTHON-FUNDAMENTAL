1 # Apa perbedaan utama antara operator = dan == ? Berikan contoh penggunaan keduanya.
# = Untuk memberi nilai atau mengisi variabel
# == Untuk membandingkan kesamaan dua nilai.
# umur = 17 (Perintah: "Jadikan umur bernilai 17!")
# umur == 17 (Pertanyaan: "Apakah umur sama dengan 17?")

2 #Manakah dari nama-nama variabel berikut yang TIIDAK VALIID di Python?
#a) _nama_depan
#b) nilai_rata2
#c) 2x
#d) namaLengkap
   #jawaban c) 2x

# 3: Apa yang akan terjadi jika kamu menjalankan kode di bawah ini dan memasukkan angka 10 ?
angka_favorit = input("Masukkan angka favoritmu: ")
hasil = angka_favorit * 2
print(hasil)
#a) Program akan menampilkan 20 .
#b) Program akan menampilkan 1010 .
#c) Program akan menampilkan 100 .
#d) Program akan mengalami TypeError .
    #jawaban b) program akan menampilkan 1010 (jika saya memasukan angka 10)

# 4: Buatlah sebuah program kecil yang melakukan hal berikut:
#1. Meminta pengguna memasukkan alas sebuah segitiga.
#2. Meminta pengguna memasukkan tinggi sebuah segitiga.
#3. Menghitung luas segitiga dengan rumus 0.5 * alas * tinggi .
#4. Menampilkan hasilnya ke layar.
#5. Tambahkan komentar di setiap baris untuk menjelaskan fungsi dari kode tersebut.
#Petunjuk: Hati-hati dengan tipe data dari input() !
  #jawaban di bawah !
alas = float(input("Masukkan alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))
luas = 0.5 * alas * tinggi
print("Luas segitiga adalah", luas)