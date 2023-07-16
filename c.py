
import sys

# Tampilkan pesan permintaan masukan
print("Masukkan data:")

# Baca masukan dari pengguna
input_data = sys.stdin.readlines()

# Tentukan file untuk menyimpan hasil
file = open('coba.txt', 'w')

# Untuk setiap baris data masukan
for line in input_data:
    # Tulis baris data masukan ke dalam file
    file.write(line)

# Tutup file
file.close()

# Tampilkan pesan sukses
print("Data berhasil disimpan di file coba.txt")
