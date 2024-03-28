def hitung_gaji(hari_kerja, gaji_per_hari, tarif_lembur):
    if hari_kerja > 25:
        hari_lembur = hari_kerja - 25
        gaji_total = (25 * gaji_per_hari) + (hari_lembur * tarif_lembur)
    else:
        gaji_total = hari_kerja * gaji_per_hari
    return gaji_total

# Input dari pengguna
hari_kerja = int(input("masukkan hari kerja anda :"))
gaji_per_hari = float("200000")
tarif_lembur = float("100000")

# Hitung gaji karyawan
gaji_total = hitung_gaji(hari_kerja, gaji_per_hari, tarif_lembur)

# Output hasil
print(f"Gaji karyawan untuk {hari_kerja} hari kerja adalah: {gaji_total:,.2f}")
