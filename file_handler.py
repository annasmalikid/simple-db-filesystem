import os
import datetime

FOLDER_NAME = "mahasiswa_db"

def init_folder():
    """Memastikan folder penyimpanan tersedia."""
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)

def get_path(nim):
    """Mendapatkan lokasi file lengkap berdasarkan NIM."""
    return os.path.join(FOLDER_NAME, f"{nim}.txt")

def buat_file(nim, nama):
    filepath = get_path(nim)
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filepath, "w") as file:
        file.write(f"NAMA     : {nama}\n")
        file.write(f"NIM      : {nim}\n")
        file.write(f"DIBUAT   : {waktu}\n")
        file.write(f"STATUS   : AKTIF")
    print(f"[SUCCESS] Data {nim} berhasil disimpan.")

def baca_file(nim):
    filepath = get_path(nim)
    if os.path.exists(filepath):
        print(f"\n--- ISI DATA FILE: {nim}.txt ---")
        with open(filepath, "r") as file:
            print(file.read())
        print("--------------------------------")
    else:
        print(f"[ERROR] File dengan NIM {nim} tidak ditemukan.")

def update_huruf_besar(nim):
    """Mengubah isi file menjadi UPPERCASE dan update waktu."""
    filepath = get_path(nim)
    if os.path.exists(filepath):
        with open(filepath, "r+") as file:
            content = file.read()
            
            file.seek(0)
            
            file.write(content.upper())
            file.truncate()
            
        print(f"[SUCCESS] Data {nim} berhasil diubah ke HURUF BESAR.")
        baca_file(nim) 
    else:
        print(f"[ERROR] File NIM {nim} tidak ditemukan.")

def hapus_file(nim):
    filepath = get_path(nim)
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"[DELETED] File data {nim} telah dihapus permanen.")
    else:
        print(f"[ERROR] File tidak ditemukan, tidak ada yang dihapus.")


def main():
    init_folder()
    
    while True:
        print("\n=== FILE RECORD MANAGER ===")
        print("1. Buat Data Baru")
        print("2. Lihat Data")
        print("3. Ubah ke Huruf Besar (Update)")
        print("4. Hapus Data")
        print("0. Keluar")
        
        pilihan = input(">> Pilih menu: ")

        if pilihan == "1":
            nim = input("Masukkan NIM  : ")
            nama = input("Masukkan Nama : ")
            buat_file(nim, nama)
        
        elif pilihan == "2":
            nim = input("Masukkan NIM yang dicari: ")
            baca_file(nim)

        elif pilihan == "3":
            nim = input("Masukkan NIM untuk di-update: ")
            update_huruf_besar(nim)

        elif pilihan == "4":
            nim = input("Masukkan NIM untuk dihapus: ")
            hapus_file(nim)

        elif pilihan == "0":
            print("Terima kasih. Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
