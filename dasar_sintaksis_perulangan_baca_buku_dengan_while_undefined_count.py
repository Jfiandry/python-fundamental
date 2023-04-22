"""
Program perulangan membaca buku dengan while
"""
jumlah_buku = 10
print('Perintah ibu, "Baca dan pahami semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0
jumlah_buku_yang_dipahami = 0
print(f'jumlah buku yang sudah dibaca dan dipahami adalah {jumlah_buku_yang_dipahami} buku')

while jumlah_buku_yang_sudah_dibaca < jumlah_buku * 2:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    if jumlah_buku_yang_dipahami == 9:
        print(f"buku ke {jumlah_buku_yang_dipahami + 1} belum paham")
    else:
        jumlah_buku_yang_dipahami = jumlah_buku_yang_dipahami + 1
        print(f"buku ke {jumlah_buku_yang_dipahami} yang sudah dibaca dan dipahami")

print(f"buku ke {jumlah_buku_yang_dipahami + 1} belum paham")
print(f"buku sudah dibaca {jumlah_buku_yang_sudah_dibaca} kali")
print(f"jumlah buku yang sudah dibaca dan dipahami adalah {jumlah_buku_yang_dipahami} buku")

if jumlah_buku_yang_dipahami == jumlah_buku:
    print('Bu, semua buku sudah dibaca dan dipahami')
else:
    print(f"Bu, tidak semua buku bisa dipahami. Budi hanya bisa memahami sebanyak {jumlah_buku_yang_dipahami} buku")
