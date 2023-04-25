print("\nPerintah del dengan list comperhensive")
daftar_buku = ["Seven Wonder", "One Piece", "First Thing", "bleach"]
del daftar_buku[:]          #del [:] berfungsi untuk menghapus keseluruhan daftar_buku
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del")
daftar_buku = ["Seven Wonder", "One Piece", "First Thing", "bleach"]
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comperhensive start-end")
daftar_buku = ["Seven Wonder", "One Piece", "First Thing", "bleach"]
del daftar_buku[0:2]                 #start:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comperhensive start-end-step")
daftar_buku = ["Seven Wonder", "One Piece", "First Thing", "bleach"]
del daftar_buku[0:4:2]                 #start:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMembuat list baru")
daftar_buku = ["Seven Wonder", "One Piece", "First Thing", "bleach"]
daftar_buku_baru = daftar_buku[:]
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat list baru dengan comprehension: ganjil")
daftar_buku = ["Seven Wonder", "One Piece", "First Thing", "bleach"]
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat list baru dengan comprehension: genap")
daftar_buku = ["Seven Wonder", "One Piece", "First Thing", "bleach"]
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat list baru dengan comprehension: buang di ujung")
daftar_buku = ["Seven Wonder", "One Piece", "First Thing", "bleach"]
daftar_buku_baru = daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print(daftar_buku[0::2])




