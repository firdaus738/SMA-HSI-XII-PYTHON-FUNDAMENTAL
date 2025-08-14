#1
def buat_email(nama_pengguna, domain="coding.com"):
    return f"{nama_pengguna.lower()}@{domain.lower()}"

print(buat_email("Budi"))              
print(buat_email("Ani", "belajar.id")) 

#2
def kirim_paket(barang, tujuan, berat_kg, asuransi=False, express=False):
    print(f"Mengirim {barang} ke {tujuan}, berat {berat_kg}kg, express={express}, asuransi={asuransi}")

kirim_paket(barang="Buku", tujuan="Bandung", berat_kg=2, express=True)

#3
def analisis_daftar(daftar_angka):
    total = sum(daftar_angka)
    jumlah_elemen = len(daftar_angka)
    rata_rata = total / jumlah_elemen
    return total, jumlah_elemen, rata_rata

angka = [10, 20, 30, 40, 50]
total, jumlah, rata2 = analisis_daftar(angka)

print("Total:", total)
print("Jumlah elemen:", jumlah)
print("Rata-rata:", rata2)

#4
def analisis_daftar(daftar_angka):
    """
    Menganalisis daftar angka dan mengembalikan total, jumlah elemen, dan rata-ratanya.

    Args:
        daftar_angka (list): Daftar angka (int atau float).

    Returns:
        tuple: (total, jumlah elemen, rata-rata)
    """
    total = sum(daftar_angka)
    jumlah_elemen = len(daftar_angka)
    rata_rata = total / jumlah_elemen
    return total, jumlah_elemen, rata_rata

help(analisis_daftar)

#5
luas_lingkaran_lambda = lambda radius: 3.14159 * (radius ** 2)

# Pengujian:
print(luas_lingkaran_lambda(7))  