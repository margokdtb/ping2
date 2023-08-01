import os
import shutil

# Mendapatkan nama folder saat ini
current_folder = os.getcwd()

# Menentukan path folder subdomain
subdomain_folder = os.path.join(current_folder, 'subdomain')

# Mengecek apakah folder subdomain ada
if os.path.exists(subdomain_folder):
    # Mengambil daftar file di dalam folder subdomain
    files = os.listdir(subdomain_folder)
    
    # Menampilkan semua file di dalam folder subdomain
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")
    
    # Meminta pengguna memilih nomor file yang ingin disalin
    choice = input("Pilih nomor file : ")
    
    try:
        # Mengonversi pilihan pengguna menjadi indeks file yang benar
        file_index = int(choice) - 1
        
        # Memilih file yang sesuai dengan indeks yang dipilih
        selected_file = files[file_index]
        
        # Mengonversi path file menjadi absolut
        file_path = os.path.join(subdomain_folder, selected_file)
        
        # Mengcopy file yang dipilih ke folder sebelumnya dan mengganti namanya menjadi subdomain.txt
        shutil.copy(file_path, os.path.join(current_folder, 'subdomain.txt'))
        
        print("File telah dipilih")
    except IndexError:
        print("Nomor file yang dimasukkan tidak valid.")
else:
    print("Folder subdomain tidak ditemukan.")