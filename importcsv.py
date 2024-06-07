import csv

# Data siswa
data_siswa = [
    {"nama": "Andi", "kelas": "10A", "jenis_kelamin": "Laki-Laki", "tempat_lahir": "Jakarta", "tanggal_lahir": "2006-04-15", "agama": "Islam", "ayah": "Budi", "pekerjaan_ayah": "Pegawai Negeri", "ibu": "Siti", "pekerjaan_ibu": "Ibu Rumah Tangga", "usia": 18},
    {"nama": "Budi", "kelas": "11B", "jenis_kelamin": "Laki-Laki", "tempat_lahir": "Bandung", "tanggal_lahir": "2005-08-20", "agama": "Kristen", "ayah": "Tono", "pekerjaan_ayah": "Pengusaha", "ibu": "Rina", "pekerjaan_ibu": "Guru", "usia": 18},
    {"nama": "Citra", "kelas": "12C", "jenis_kelamin": "Perempuan", "tempat_lahir": "Surabaya", "tanggal_lahir": "2004-12-05", "agama": "Hindu", "ayah": "Agus", "pekerjaan_ayah": "Dokter", "ibu": "Wati", "pekerjaan_ibu": "Perawat", "usia": 19},
    {"nama": "Dewi", "kelas": "10A", "jenis_kelamin": "Perempuan", "tempat_lahir": "Yogyakarta", "tanggal_lahir": "2006-02-18", "agama": "Buddha", "ayah": "Eka", "pekerjaan_ayah": "Polisi", "ibu": "Sri", "pekerjaan_ibu": "Pengacara", "usia": 18},
    {"nama": "Eko", "kelas": "11B", "jenis_kelamin": "Laki-Laki", "tempat_lahir": "Medan", "tanggal_lahir": "2005-06-22", "agama": "Islam", "ayah": "Dedi", "pekerjaan_ayah": "Petani", "ibu": "Lestari", "pekerjaan_ibu": "Pedagang", "usia": 19}
]

# Nama file CSV
filename = "data_siswa.csv"

# Menulis data ke file CSV
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data_siswa[0].keys())
    writer.writeheader()
    writer.writerows(data_siswa)

print(f"Data siswa berhasil disimpan ke dalam file {filename}")
