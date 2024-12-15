def hitung_biaya_pengiriman(): 
    #input lokasi
    lokasi = input("Masukkan lokasi pengiriman (Kota/Kabupaten Pasuruan): ").strip().lower()
    if lokasi not in ["kota pasuruan", "kabupaten pasuruan"]:
        print("Maaf, layanan hanya tersedia untuk area Kota dan Kabupaten Pasuruan.")
        return
    
    #input dimensi paket
    panjang = float(input("Masukkan panjang paket (cm): "))
    lebar = float(input("Masukkan lebar paket (cm): "))
    tinggi = float(input("Masukkan tinggi paket (cm): "))
    berat = float(input("Masukkan berat paket (kg): "))
    
    #berat minimal adalah 1 kg
    if berat < 1:
        berat = 1
        print("Berat paket dianggap minimal 1 kg.")
    
    #perhitungan volume paket
    volume = panjang * lebar * tinggi
    
    #perhitungan biaya
    if panjang <= 50 and lebar <= 50 and tinggi <= 50:
        biaya_per_kg = 5000
        biaya_total = max(8000, berat * biaya_per_kg)  # Minimal biaya 8000
    else:
        biaya_per_kg = 7000
        biaya_total = max(8000, berat * biaya_per_kg + 50000)  # Tambahan 50.000
    
    #menampilkan hasil
    print(f"Lokasi pengiriman: {lokasi.capitalize()}")
    print(f"Dimensi paket: {panjang}cm x {lebar}cm x {tinggi}cm")
    print(f"Berat paket: {berat} kg")
    print(f"Biaya pengiriman: Rp {biaya_total:,}")
    
#menjalankan program
hitung_biaya_pengiriman()