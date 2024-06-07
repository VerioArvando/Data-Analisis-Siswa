import matplotlib.pyplot as plt

# Data siswa
data_siswa = [
    {"nama": "Andi", "kelas": "10A", "jenis_kelamin": "Laki-Laki", "tempat_lahir": "Jakarta", "tanggal_lahir": "2006-04-15", "agama": "Islam", "ayah": "Budi", "pekerjaan_ayah": "Pegawai Negeri", "ibu": "Siti", "pekerjaan_ibu": "Ibu Rumah Tangga", "usia": 18},
    {"nama": "Budi", "kelas": "11B", "jenis_kelamin": "Laki-Laki", "tempat_lahir": "Bandung", "tanggal_lahir": "2005-08-20", "agama": "Kristen", "ayah": "Tono", "pekerjaan_ayah": "Pengusaha", "ibu": "Rina", "pekerjaan_ibu": "Guru", "usia": 18},
    {"nama": "Citra", "kelas": "12C", "jenis_kelamin": "Perempuan", "tempat_lahir": "Surabaya", "tanggal_lahir": "2004-12-05", "agama": "Hindu", "ayah": "Agus", "pekerjaan_ayah": "Dokter", "ibu": "Wati", "pekerjaan_ibu": "Perawat", "usia": 19},
    {"nama": "Dewi", "kelas": "10A", "jenis_kelamin": "Perempuan", "tempat_lahir": "Yogyakarta", "tanggal_lahir": "2006-02-18", "agama": "Buddha", "ayah": "Eka", "pekerjaan_ayah": "Polisi", "ibu": "Sri", "pekerjaan_ibu": "Pengacara", "usia": 18},
    {"nama": "Eko", "kelas": "11B", "jenis_kelamin": "Laki-Laki", "tempat_lahir": "Medan", "tanggal_lahir": "2005-06-22", "agama": "Islam", "ayah": "Dedi", "pekerjaan_ayah": "Petani", "ibu": "Lestari", "pekerjaan_ibu": "Pedagang", "usia": 19}
]

# Ekstraksi data
usia = [siswa["usia"] for siswa in data_siswa]
agama = [siswa["agama"] for siswa in data_siswa]
tempat_lahir = [siswa["tempat_lahir"] for siswa in data_siswa]

# Histogram Usia
plt.figure(figsize=(10, 5))
plt.hist(usia, bins=5, edgecolor='black')
plt.title('Histogram Usia Siswa')
plt.xlabel('Usia')
plt.ylabel('Jumlah Siswa')
plt.grid(True)
plt.show()

# Pie Chart Agama
agama_count = {a: agama.count(a) for a in set(agama)}
plt.figure(figsize=(8, 8))
plt.pie(agama_count.values(), labels=agama_count.keys(), autopct='%1.1f%%')
plt.title('Distribusi Agama Siswa')
plt.show()

# Diagram Garis Tempat Lahir
tempat_lahir_count = {t: tempat_lahir.count(t) for t in set(tempat_lahir)}
plt.figure(figsize=(10, 5))
plt.plot(list(tempat_lahir_count.keys()), list(tempat_lahir_count.values()), marker='o')
plt.title('Distribusi Tempat Lahir Siswa')
plt.xlabel('Tempat Lahir')
plt.ylabel('Jumlah Siswa')
plt.grid(True)
plt.show()
