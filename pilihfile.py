import os
import shutil

# Menampilkan isi folder
def list_files(folder):
    print("Daftar file dengan kata depan 'subdo_':")
    for filename in os.listdir(folder):
        if filename.startswith("subdo_"):
            print(filename)

# Mendapatkan alamat folder saat ini
current_folder = os.path.dirname(os.path.realpath(__file__))

# Memilih file dengan kata depan 'subdo_' untuk dicopy dan diganti namanya
def copy_and_rename_file(source_folder):
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f)) and f.startswith("subdo_")]

    if len(files) == 0:
        print("Tidak ada file dengan kata depan 'subdo_' dalam folder ini.")
        return

    print("\nDaftar file :")
    for i, filename in enumerate(files):
        print(f"{i+1}. {filename}")
    choice = input("Pilih nomor file : ")

    try:
        index = int(choice) - 1
        old_filename = files[index]
        new_filename = "subdomain.txt"
        shutil.copy(os.path.join(source_folder, old_filename), os.path.join(source_folder, new_filename))
        print(f"\nFile {old_filename} telah dipilih ")
    except (ValueError, FileNotFoundError, IndexError):
        print("\nPilihan file tidak valid")

# Main program
folder_path = current_folder  # Menggunakan folder saat ini sebagai sumber folder
#list_files(folder_path)
copy_and_rename_file(folder_path)