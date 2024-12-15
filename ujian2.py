def hitung_biaya_parkir(jam,jenis_kendaraan):
    #input jenis kendaraan {hanya motor/mobil} dan penjelasan biaya
    if jenis_kendaraan == "motor":
        tarif_awal = 3000
        tarif_per_jam = 1000
    elif jenis_kendaraan == "mobil":
        tarif_awal = 3000
        tarif_per_jam = 1500
    else:
        return "jenis kendaraan tidak valid"   
    #input tarif tambahan
    tarif_tambahan_24jam = 10000
    #hitung biaya parkir
    if jam <= 2:
        biaya = tarif_awal
    elif jam <= 24:
        biaya = tarif_awal + (jam - 2) * tarif_per_jam
    else:
        biaya = tarif_awal + (jam - 2) * tarif_per_jam + tarif_tambahan_24jam
#menampilkan hasil perhitungan biaya parkir
    return biaya
#menanyakan jenis kendaraan
jenis_kendaraan = input("Masukkan jenis kendaraan motor/mobil? ").strip().lower()                     
#hanya bisa motor/mobil yang parkir
if jenis_kendaraan not in ["motor","mobil"]:
    print("Maaf parkir hanya bisa mobil dan motor.")
#input jam parkir
else:
    jumlah_jam = input("Masukkan berapa jam anda parkir: ").strip()

    if jumlah_jam.isdigit():
        jumlah_jam = int(jumlah_jam)
        #jumlah jam harus diatas 0
        if jumlah_jam <= 0:
            print("maaf, masukkan angka yang lebih besar dari 0")
            #menampilkan hasil
        else:
            biaya= hitung_biaya_parkir(jumlah_jam, jenis_kendaraan)
            print(f"Biaya parkir untuk {jenis_kendaraan} selama {jumlah_jam} jam adalah {biaya:,}")
        #hanya bisa memasukkan angka
    else:
        print("Masukkan angka yang valid untuk jam parkir")