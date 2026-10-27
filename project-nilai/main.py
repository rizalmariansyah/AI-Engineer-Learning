import os

os.system("cls" if os.name == "nt" else "clear")

print("=== Program Nilai Siswa ===")

mahasiswa = {"Andi": 80, "Budi": 75, "Citra": 90, "Dina": 70}

jumlah_lulus = 0
jumlah_tidak_lulus = 0

for nama, nilai in mahasiswa.items():
    if nilai >= 75:
        status = "lulus"
        jumlah_lulus += 1
    else:
        status = "tidak lulus"
        jumlah_tidak_lulus += 1
    print(f"nama: {nama} |  nilai: {nilai} | status: {status}")


nilai = mahasiswa.values()
jumlah_mahasiswa = len(mahasiswa)
total_nilai = sum(nilai)
rata_rata = total_nilai / jumlah_mahasiswa
nilai_tertinggi = max(nilai)
nilai_terendah = min(nilai)

print(f"\nJumlah Mahasiswa: {jumlah_mahasiswa}")
print(f"Jumlah Lulus: {jumlah_lulus}")
print(f"Jumlah Tidak Lulus: {jumlah_tidak_lulus}")
print(f"Total Nilai: {total_nilai}")
print(f"Rata-rata Nilai: {rata_rata}")
print(f"Nilai tertinggi: {nilai_tertinggi}")
print(f"Nilai terendah: {nilai_terendah}")


for nama, nilai in mahasiswa.items():
    if nilai == nilai_tertinggi:
        print(f"\nnama mahasiswa nilai tertinggi adalah: {nama}")
    elif nilai == nilai_terendah:
        print(f"nama mahasiswa nilai terendah adalah: {nama}")

cari_nama = input("\nmasukan nama yang dicari: ")


if cari_nama in mahasiswa :
    print("nama :",cari_nama)
    print ("nilai :", mahasiswa[cari_nama])
    print ("status :", mahasiswa[cari_nama])
else:
    print ("nama tidak ditemukan")



