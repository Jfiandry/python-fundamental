"""
Program perulangan membaca buku dengan for
"""
jumlah_buku = 10
print('Perintah ibu, "Baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0
for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1):
    print(f"buku ke {jumlah_buku_yang_sudah_dibaca} yang sudah dibaca")

print(f"jumlah buku yang sudah dibaca adalah {jumlah_buku_yang_sudah_dibaca} buku")
