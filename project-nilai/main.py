import os

os.system("cls" if os.name == "nt" else "clear")

print("=== Program Nilai Siswa ===")

mahasiswa = {
    "Andi": 80,
    "Budi": 75,
    "Citra": 90
}


for nama,nilai in mahasiswa.items():
    if nilai >= 75:
        status = "lulus"
    else:
        status = "tidak lulus"
    print(f"nama: {nama} |  nilai: {nilai} | status: {status}")
       



nilai = mahasiswa.values()
jumlah_mahasiswa = len(mahasiswa)
total_nilai = sum(nilai)
rata_rata = total_nilai / jumlah_mahasiswa

print(f"\nJumlah Mahasiswa: {jumlah_mahasiswa}")
print(f"Total Nilai: {total_nilai}")
print(f"Rata-rata Nilai: {rata_rata}")


