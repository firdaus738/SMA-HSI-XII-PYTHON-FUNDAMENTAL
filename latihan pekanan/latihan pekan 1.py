print("="*43)
print("SELAMAT DATANG DI PROGRAM KASIR CERDAS!".center(43))
print("="*43)

# Input Barang 1
print("\n--- Masukkan Detail Barang 1 ---")
nama_barang_1 = input("Nama Barang: ")
harga_1 = float(input("Harga Satuan (Rp): "))
jumlah_1 = int(input("Jumlah: "))

# Input Barang 2
print("\n--- Masukkan Detail Barang 2 ---")
nama_barang_2 = input("Nama Barang: ")
harga_2 = float(input("Harga Satuan (Rp): "))
jumlah_2 = int(input("Jumlah: "))

# Hitung total per barang
total_1 = harga_1 * jumlah_1
total_2 = harga_2 * jumlah_2

# Subtotal
subtotal = total_1 + total_2

# Logika Diskon

if subtotal > 200000:
    diskon_persen = 10
elif subtotal > 100000:
    diskon_persen = 5
else :
    diskon_persen = 0

jumlah_diskon = subtotal * diskon_persen / 100
total_setelah_diskon = subtotal - jumlah_diskon

# Tambahkan PPN (opsional / tantangan)
ppn = total_setelah_diskon * 11 / 100
total_akhir = total_setelah_diskon + ppn

print("-"*43)
print(f"{'-'*3} JUMLAH PEMBELIAN ANDA {'-'*3}")
print("Detail Belanja:")
print(f"1. {nama_barang_1} ({jumlah_1} x Rp {harga_1:,.2f}) = Rp {total_1:,.2f}")
print(f"2. {nama_barang_2} ({jumlah_2} x Rp {harga_2:,.2f}) = Rp {total_2:,.2f}")
print("-"*43)
print(f"Subtotal           : Rp {subtotal:,.2f}")
print(f"Diskon             : - Rp {jumlah_diskon:,.2f}")
print(f"PPN (11%)         : + Rp {ppn:,.2f}")
print("-"*43)
print(f"Total yang harus dibayar: Rp {total_akhir:,.2f}")


# Minta jumlah uang dari pelanggan
print("\n--- Pembayaran ---")
uang_dibayar = float(input("Jumlah uang yang dibayarkan pelanggan (Rp): "))
kembalian = uang_dibayar - total_akhir

# Cetak Struk
print("="*43)
print(" STRUK PEMBELIAN ANDA".center(43))
print("="*43)
print("Detail Belanja:")
print(f"1. {nama_barang_1} ({jumlah_1} x Rp {harga_1:,.2f}) = Rp {total_1:,.2f}")
print(f"2. {nama_barang_2} ({jumlah_2} x Rp {harga_2:,.2f}) = Rp {total_2:,.2f}")
print("-"*43)
print(f"Subtotal          : Rp {subtotal:,.2f}")
print(f"Diskon ({diskon_persen}%)     : - Rp {jumlah_diskon:,.2f}")
print(f"PPN (11%)         : + Rp {ppn:,.2f}")
print("-"*43)
print(f"Total Dibayar     : Rp {total_akhir:,.2f}")
print(f"Uang Diberikan    : Rp {uang_dibayar:,.2f}")
print(f"Kembalian         : Rp {kembalian:,.2f}")
print("="*43)
print("TERIMA KASIH TELAH BERBELANJA!".center(43))
print("="*43)