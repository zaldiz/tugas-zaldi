class Perpustakaan:
    def __init__(self):
        self.koleksi_buku = []

    def check_ketersediaan(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                if buku.status == "Tersedia":
                    print(f"Buku {buku.judul} tersedia untuk dipinjam.")
                else:
                    print(f"Buku {buku.judul} tidak tersedia untuk dipinjam.")
                return
        print(f"Buku dengan judul '{judul}' tidak ditemukan.")

    def tampilkan_buku(self):
        if self.koleksi_buku:
            print("-- Daftar Buku --")
            for buku in self.koleksi_buku:
                print(buku)
        else:
            print("Koleksi buku masih kosong.")

    def cari_buku(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                print(buku)
                return
        print(f"Buku dengan judul '{judul}' tidak ditemukan.")

    def pinjam__buku(self, judul, anggota):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                if buku.status == "Tersedia":
                    buku.status = "Dipinjam"
                    anggota.buku_pinjaman.append(buku)
                    print(f"Buku '{buku.judul}' berhasil dipinjam oleh {anggota.nama}.")
                else:
                    print(f"Buku '{buku.judul}' tidak tersedia untuk dipinjam.")
                return
        print(f"Buku dengan judul '{judul}' tidak ditemukan.")

class Anggota:
    def __init__(self, nama, ID):
        self.nama = nama
        self.ID = ID
        self.buku_pinjaman = []

    def tampilkan_buku_pinjaman(self):
        if self.buku_pinjaman:
            print(f"-- Buku Pinjaman {self.nama} --")
            for buku in self.buku_pinjaman:
                print(buku)
        else:
            print(f"{self.nama} tidak memiliki buku pinjaman.")

class Buku:
    def __init__(self, judul, penulis, genre, status):
        self.judul = judul
        self.penulis = penulis
        self.genre = genre
        self.status = status

    def __str__(self):
        return f"{self.judul} - {self.penulis} ({self.genre}) - Status: {self.status}"

def main():
    # Buat beberapa buku
    bukul = Buku("Bumi", "Tere Liye", "Fiksi", "Tersedia")
    buku2 = Buku("Laskar Pelangi", "Andrea Hirata", "Fiksi", "Tersedia")
    buku3 = Buku("Filosofi Terbang", "Dewi Lastari", "Fiksi", "Dipinjam")

    # Buat perpustakaan
    perpustakaan = Perpustakaan()
    perpustakaan.koleksi_buku.extend([bukul, buku2, buku3])

    # Buat anggota
    anggota1 = Anggota("Adi", 12345)
    anggota2 = Anggota("Adu", 56789)

    # Jalankan program
    print("\n-- Menu Perpustakaan --")
    print("1. Tampilkan Daftar Buku")
    print("2. Cari Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan")
    angka = int(input("Pilih menu: "))

    if angka == 1:
        perpustakaan.tampilkan_buku()
    elif angka == 2:
        judul = input("Masukkan judul buku: ")
        perpustakaan.cari_buku(judul)
    elif angka == 3:
        judul = input("Judul buku yang akan dipinjam: ")
        perpustakaan.pinjam__buku(judul, anggota1)  # Peminjaman buku oleh anggota1, bisa disesuaikan dengan anggota lain
    elif angka == 4:
        pass  # Logika untuk pengembalian buku belum diimplementasikan
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main();
