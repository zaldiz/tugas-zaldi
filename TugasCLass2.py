kelas Buku:
    def __init__(diri, judul, penulis, genre, status):
        self.judul = judul
        self.penulis = penulis
        self.genre = genre
        diri.status = status

    def __str__(diri):
        return f"{self.judul} - {self.penulis} ({self.genre}) - Status: {self.status}"

perpustakaan kelas:
    def __init__(diri):
        diri.koleksi_buku = []

    def check_ketersediaan(mandiri):
        jika tidak mandiri.buku.tersedia:
            print(f"Buku {self.buku.judul}' tidak tersedia untuk dipinjamkan.")

    def tampilkan_buku(diri):
        if self.koleksi_buku:
            print("-- Daftar Buku --")
            untuk buku di self.koleksi_buku:
                mencetak (buku)
        kalau tidak:
            print("Koleksi buku masih kosong.")

    def cari_buku(self, judul):
        untuk buku di self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                mencetak (buku)
                kembali
        print(f"Buku dengan judul '{judul} tidak ditemukan.")

    def pinjam_buku(diri, judul, anggota):
        untuk buku di self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                if buku.status == "Tersedia":
                    buku.status = "Dipinjam"
                    anggota.buku_pinjaman.append(buku)
                    print(f"Buku {buku.judul}' berhasil dipinjamkan oleh {anggota.nama}.")
                    kembali
                kalau tidak:
                    print(f"Buku {buku.judul}' tidak tersedia untuk dipinjamkan.")
                    kembali
        print(f"Buku dengan judul '{judul}' tidak ditemukan.")

anggota kelas:
    def __init__(diri, nama, ID, alamat=Tidak ada, nomor_telepon=Tidak ada):
        diri.nama = nama
        diri.ID = ID
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
        mandiri.buku_pinjaman = []

    def tampilkan_buku_pinjaman(self):
        if self.buku_pinjaman:
            print(f"-- Buku Pinjaman {self.nama} --")
            untuk buku di self.buku_pinjaman:
                mencetak (buku)
        kalau tidak:
            print(f"{self.nama} tidak memiliki buku pinjaman.")

kelas Catatan_peminjaman:
    def __init__(diri, id_buku, id_anggota, tanggal_pinjam, tanggal_kembali):
        diri.id_buku = id_buku
        diri.id_anggota = id_anggota
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali                

def utama():
    # Buat beberapa buku
    buku1 = Buku("Bumi", "Tere Liye", "Fiksi", "Tersedia")
    buku2 = Buku("Laskar Pelangi", "Andrea Hirata", "Fiksi", "Tersedia")
    buku3 = Buku("Filosofi Terbang", "Dewi Lestari", "Fiksi", "Dipinjam")

    # Buat perpustakaan
    perpustakaan = Perpustakaan()
    perpustakaan.koleksi_buku.extend([buku1, buku2, buku3])

    #Buat anggota
    anggota1 = Anggota("Adi", 12345)
    anggota2 = Anggota("Adu", 56789)

    #Program Jalankan
    print("\n-- Menu Perpustakaan --")
    print("1.Tampilkan Daftar Buku")
    print("2.Cari Buku")
    print("3.Pinjam Buku")
    print("4.Kembalikan")
    angka = int(input("Pilih menu : "))

    jika angka == 1:
        perpustakaan.tampilkan_buku()
    elif angka == 2:
        judul = input("Masukkan judul buku : ")
        perpustakaan.cari_buku(judul)
    elif angka == 3:
        judul = input("Judul buku yang akan dipinjamkan : ")
        perpustakaan.pinjam_buku(judul, anggota1)
    elif angka == 4:
        buku = input("Judul buku yang akan dikembalikan : ")
        # Tambahkan logika untuk mengembalikan buku
    kalau tidak:
        print("Anda salah memilih.")

jika _nama_ == "_utama_":
    utama()
