
def tampilkan_header():
    print("=" * 42)
    print(" SELAMAT DATANG DI TOKO SERBAGUNA".center(42))
    print("=" * 42)



def get_numeric_input(prompt):
    while True:
        try:
            nilai = float(input(prompt))
            return nilai
        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")



def hitung_subtotal(daftar_harga, daftar_jumlah):
    total = 0
    for i in range(len(daftar_harga)):
        total += daftar_harga[i] * daftar_jumlah[i]
    return total



def hitung_diskon(subtotal):
    if subtotal >= 500000:
        persen_diskon = 10
    elif subtotal >= 200000:
        persen_diskon = 5
    else:
        persen_diskon = 0
    jumlah_diskon = (persen_diskon / 100) * subtotal
    return jumlah_diskon, persen_diskon



def tampilkan_struk(nama_barang, harga_barang, jumlah_barang, subtotal, diskon, persen_diskon):
    print("=" * 42)
    print(" STRUK PEMBELIAN ANDA".center(42))
    print("=" * 42)
    print("Detail Belanja:")
    for i in range(len(nama_barang)):
        total_per_item = harga_barang[i] * jumlah_barang[i]
        
        jumlah = jumlah_barang[i]
    if jumlah == int(jumlah):
        jumlah_str = str(int(jumlah))
    else:
        jumlah_str = str(jumlah)


    print(f"{i+1}. {nama_barang[i]} ({jumlah_str} x {harga_barang[i]:,.2f}) = {total_per_item:,.2f}")
    
    print("-" * 42)
    print(f"Subtotal              : {(subtotal):,.2f}")
    print(f"Diskon ({persen_diskon}%)          : - {(diskon):,.2f}")
    print("-" * 42)
    print(f"Total yang harus dibayar: {(subtotal - diskon):,.2f}")
    print("=" * 42)
    print(" TERIMA KASIH TELAH BERBELANJA!".center(42))
    print("=" * 42)



daftar_nama_barang = []
daftar_harga_barang = []
daftar_jumlah_barang = []

tampilkan_header()


print("--- Masukkan Detail Barang ---")

print("(Ketik 'selesai' di nama barang untuk selesai)")

while True:
    nama = input("Nama Barang: ")
    if nama.lower() == "selesai":
        break

    harga = get_numeric_input("Harga Satuan: Rp ")
    jumlah = get_numeric_input("Jumlah: ")

    daftar_nama_barang.append(nama)
    daftar_harga_barang.append(harga)
    daftar_jumlah_barang.append(jumlah)

    print("--- Barang berhasil ditambahkan! ---")

print("\nMenghitung total belanja Anda...")


subtotal = hitung_subtotal(daftar_harga_barang, daftar_jumlah_barang)
diskon, persen_diskon = hitung_diskon(subtotal)

# Tampilkan struk
tampilkan_struk(
    daftar_nama_barang,
    daftar_harga_barang,
    daftar_jumlah_barang,
    subtotal,
    diskon,
    persen_diskon
)