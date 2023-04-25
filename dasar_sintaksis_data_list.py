daftar_buku = ["Seven Wonder", "One Piece", "First Thing"]
print("tampilkan variabel daftar_buku")
print(daftar_buku)

print("\nProses semua dengan For in")
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'kenji Volume 2', -313, 3, 14]
print('\nTampilkan dengan for in range dengan elemen variabel yang berbeda2')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nkembalikan nilai awal daftar_buku')
daftar_buku = ["Seven Wonder", "One Piece", "First Thing"]
daftar_buku.append("Naruto")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])



print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nganti elemen pertama")
daftar_buku = ["Seven Wonder", "One Piece", "First Thing", "bleach"]
daftar_buku[0] = "Eight Wonder"
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\n ambil elemen ke-2")
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

daftar_buku = ["Seven Wonder", "One Piece", "First Thing", "bleach"]
print('\nPop kosong')
daftar_buku.pop()             #pop kosong akan mengambil data paling akhir = bleach
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = ["Seven Wonder", "One Piece", "First Thing", "bleach"]
print('\nPop -1')
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])








