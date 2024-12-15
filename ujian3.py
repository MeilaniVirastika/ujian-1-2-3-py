def hitung_biaya_parkir (durasi):
    #input durasi parkir
    biaya_dibawah_2_jam= 3000
    biaya_diatas_2_jam= 1500
    tarif_tambahan = 5000
   #memproses biaya/menghitung
    if durasi<=2:
       biaya=biaya_dibawah_2_jam
    elif durasi> 2:
         biaya = biaya_dibawah_2_jam + (durasi-2) *biaya_diatas_2_jam

    if durasi > 24:
       biaya = biaya_dibawah_2_jam + (durasi-2) *biaya_diatas_2_jam + tarif_tambahan
       #menampilkan hasil biaya parkir
    return biaya
#input jam parkir
try:
    durasi = int(input("berapa jam anda parkir disini:"))
    #jam parkir harus lebih besar dari 0/gaboleh negatif
    if durasi < 0:
       print("Jam parkir tidak boleh negatif")
    else:
       #menampilkan hasil/biaya
       biaya = hitung_biaya_parkir (durasi)
       print(f"Biaya parkir untuk {durasi} jam adalah Rp {biaya}")
#hanya bisa masukkan angka jika tidak akan error
except ValueError:
     print("Harap masukkan angka yang valid")