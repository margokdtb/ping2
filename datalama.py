input_file = 'input_lama.txt'
output_file = 'subdomain.txt'

konfirmasi = input("Apakah Anda sudah mengisi file input_lama.txt? (y/n) ")

if konfirmasi.lower() == 'y':
    with open(input_file, 'r') as file:
        lines = file.readlines()
else:
    print("Input belum diisi. Silakan isi file input_lama.txt terlebih dahulu.")
    exit()

data = []
for line in lines:
    data.append(line.strip())

with open(output_file, 'w') as file:
    for item in data:
        file.write(item.split(':')[0].strip() + '\n')

print('Data telah disimpan di', output_file)