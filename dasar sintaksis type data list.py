daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First']
print(daftar_buku)

print('\nTampilkan index')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -1')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nList Comperhension')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[0:2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

    print('\nList Comperhension')
    daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
    del daftar_buku[0::3] #start:end:step
    for i in range(0, len(daftar_buku)):
        print(daftar_buku[i])

print('\nMembuat list baru dengan list comperhension')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])