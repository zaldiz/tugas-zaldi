class perpustakaan:
    def __init__(self):
        self.koleksi_buku = []

    # ... (kode sebelumnya)

    def kembalikan_buku(self, buku, anggota):
        if buku in anggota.buku_pinjaman:
            buku.status = "Tersedia"
            anggota.buku_pinjaman.remove(buku)
            print(f"Buku '{buku.judul}' berhasil dikembalikan oleh '{anggota.nama}'")
        else:
            print(f"Buku '{buku.judul}' tidak ada dalam daftar pinjaman '{anggota.nama}'")

class anggota:
    def __init__(self, nama, ID):
        self.nama = nama
        self.ID = ID
        self.buku_pinjaman = []

    # ... (kode sebelumnya)

def main():
    # ... (kode sebelumnya)

    while True:
        print("\n -- Welcome to Perpustakaan --")
        print("1. Tampilkan Daftar Buku")
        print("2. Cari Buku")
        print("3. Pinjam Buku")
        print("4. Kembalikan Buku")
        print("5. Keluar")
        angka = int(input("Pilih Menu :_"))

        if angka == 1:
            perpustakaan.tampilkan_buku()
        elif angka == 2:
            judul = input("Input judul buku: ")
            perpustakaan.cari_buku(judul)
        elif angka == 3:
            buku_dipinjam = input("Buku yang dipinjam: ")
            anggota_peminjam = input("Masukkan nama anggota: ")
            for buku in perpustakaan.koleksi_buku:
                if buku.judul.lower() == buku_dipinjam.lower():
                    perpustakaan.pinjam_buku(buku, next(filter(lambda a: a.nama.lower() == anggota_peminjam.lower(), [anggota1, anggota2])))
                    break
            else:
                print("Buku tidak ditemukan.")
        elif angka == 4:
            buku_dikembalikan = input("Buku yang dikembalikan: ")
            anggota_pengembalian = input("Masukkan nama anggota: ")
            for buku in perpustakaan.koleksi_buku:
                if buku.judul.lower() == buku_dikembalikan.lower():
                    perpustakaan.kembalikan_buku(buku, next(filter(lambda a: a.nama.lower() == anggota_pengembalian.lower(), [anggota1, anggota2])))
                    break
            else:
                print("Buku tidak ditemukan.")
        elif angka == 5:
            print("Terima kasih telah menggunakan Perpustakaan!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
