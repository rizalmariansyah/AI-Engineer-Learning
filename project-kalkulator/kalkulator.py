import os

os.system("cls" if os.name == "nt" else "clear")
# Untuk membersihkan layar (hanya untuk Windows)

print("=== kalkulator sederhana ===")

print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
pilihan = input("Pilih operasi (1-4):")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))


if pilihan == "1":
    print("Anda memilih Penjumlahan")
    hasil = angka1 + angka2
    print("Hasil dari", angka1, "+", angka2, "=", hasil)
elif pilihan == "2":
    print("Anda memilih Pengurangan")
    hasil = angka1 - angka2
    print("Hasil dari", angka1, "-", angka2, "=", hasil)
elif pilihan == "3":
    print("Anda memilih Perkalian")
    hasil = angka1 * angka2
    print("Hasil dari", angka1, "x", angka2, "=", hasil)
elif pilihan == "4":
    print("Anda memilih Pembagian")
    if angka2 == 0:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
    else:
        hasil = angka1 / angka2
        print("Hasil dari", angka1, ":", angka2, "=", hasil)
else:
    print("Pilihan tidak valid.")
