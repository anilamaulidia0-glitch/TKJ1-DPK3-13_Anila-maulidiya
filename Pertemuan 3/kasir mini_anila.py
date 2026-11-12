#print("===== KASIR MINI =====")

nama_barang = input("Masukkan nama barang: ")

# Input harga dengan pengecekan agar tidak error
while True:
    try:
        harga_barang = int(input("Masukkan harga barang: Rp "))
        break
    except ValueError:
        print("Input harus berupa angka! Silakan masukkan lagi.")

# Input jumlah dengan pengecekan agar tidak error
while True:
    try:
        jumlah_barang = int(input("Masukkan jumlah barang: "))
        break
    except ValueError:
        print("Input harus berupa angka! Silakan masukkan lagi.")

# Expression dan operator aritmatika
total = harga_barang * jumlah_barang

print("\n===== STRUK PEMBELIAN =====")
print("Nama barang :", nama_barang)
print("Harga       : Rp", harga_barang)
print("Jumlah      :", jumlah_barang)
print("Total       : Rp", total)

# Input uang pembayaran
while True:
    try:
        pembayaran = int(input("Uang pembayaran: Rp "))

        if pembayaran < total:
            print("Uang pembayaran kurang! Masukkan kembali.")
        else:
            break

    except ValueError:
        print("Input harus berupa angka! Silakan masukkan lagi.")
