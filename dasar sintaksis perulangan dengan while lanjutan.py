"""
Program perulangan membaca buku dengan while sampai paham
"""

jumlah_buku = 10
jumlah_paham = 0
jumlah_baca = 0

print("Baca semua buku")
print(f"jumlah buku yang sudah dibaca dan dipahami {jumlah_paham}")

while jumlah_baca < jumlah_buku *2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_paham == 9:
        print(f"Buku ke {jumlah_paham + 1} belum paham")
    else:
        jumlah_paham = jumlah_paham + 1
        print(f"Buku ke {jumlah_paham} sudah dibaca dan dipahami")

print(f"Jumlah buku yang sudah dibaca dan dipahami {jumlah_paham}")

if jumlah_paham == jumlah_buku:
    print("Semua buku sudah dibaca dan dipahami")
else:
    print(f"Tidak semua buku dibaca dan dipahami dan hanya bisa memahami {jumlah_paham} buku")
