
 # Membaca file subdomain2.txt
with open("subdomain2.txt", "r") as file:
    data = file.readlines()

# Menghapus karakter baris baru (\n) dari setiap baris
data = [line.strip() for line in data]

# Menghapus data duplikat
data_uniq = list(set(data))

# Menyimpan hasil ke file subdomain.txt
with open("subdomain.txt", "w") as file:
    for item in data_uniq:
        file.write(item + "\n")
        print(item)

# print("Data tersimpan ke file subdomain.txt")