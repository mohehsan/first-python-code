"""
Program perulangan membaca buku dengan while
"""

jumlah_buku = 10
jumlah_buku_yangsudahdibaca = 0

print("Baca semua buku")
print(f"jumlah buku yang sudah dibaca {jumlah_buku_yangsudahdibaca}")

while jumlah_buku_yangsudahdibaca < jumlah_buku:
    jumlah_buku_yangsudahdibaca = jumlah_buku_yangsudahdibaca + 1
    print(f"Buku ke {jumlah_buku_yangsudahdibaca} sudah dibaca")


print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yangsudahdibaca}")