"""
Created on 10072021 23:02:12
Update on 22072021 10:20:12

@author: Andrea
"""
JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print("==================================================")
    print(" APLIKASI SLIP GAJI ")
    print("==================================================")
    print("")
    print("")
    print("")
    

    nama = input (">> Masukkan Nama Karyawan = ")
    print("")
    print("")
    
    print("Kode Golongan")
    print("-----------------------")
    print(" a = Golongan 1")
    print(" b = Golongan 2")
    print(" c = Golongan 3")
    pilihanGolongan = input(">> Masukkan Kode Golongan = ")
    print("")
    print("")
    print("")


    print("Jenis Kelamin")
    print("-----------------------")
    print(" L = Laki-Laki")
    print(" P = Perempuan")
    pilihanJenisKelamin = input(">> Masukkan Kode Jenis Kelamin = ")
    if pilihanJenisKelamin =="l" or pilihanJenisKelamin =="L":
        kelamin = "Laki-laki"
    else:
        kelamin = "Perempuan"
    print("")
    print("")
    print("")

    
    print("Status Pernikahan")
    print("-----------------------")
    print(" L = Lajang")
    print(" K = Kawin")
    pilihanPernihakan = input(">> Masukkan Kode Status Pernikahan = ")
    if pilihanPernihakan =="l" or pilihanPernihakan=="L":
        statusKawin = "Lajang"
    else:
        statusKawin = "Kawin"
    print("")
    print("")
    print("")
    




# Mulai Berhitung
# 1. Gaji Pokok
    if pilihanGolongan == "a" or pilihanGolongan =="A":
        namaGolongan = "1"
        nominalGolongan = 2500000
    elif pilihanGolongan == "b" or pilihanGolongan =="B":
        namaGolongan = "2"
        nominalGolongan = 4500000
    elif pilihanGolongan == "c" or pilihanGolongan =="C":
        namaGolongan = "3"
        nominalGolongan = 6500000

# 2. Tunjangan Istri Dan Anak
    if pilihanPernihakan == "K" or pilihanPernihakan=="k":
        if pilihanJenisKelamin == "L" or pilihanJenisKelamin == "l":
            jenisKelamin = "Laki-Laki"
            if pilihanGolongan == "a" or pilihanGolongan == "A":
                tunjanganIstri = nominalGolongan*(1/100)
                tunjanganAnak = nominalGolongan*(2/100)
            elif pilihanGolongan == "b" or pilihanGolongan =="B":
                tunjanganIstri = nominalGolongan*(3/100)
                tunjanganAnak = nominalGolongan*(2/100)
            elif pilihanGolongan == "c" or pilihanGolongan =="C":
                tunjanganIstri = nominalGolongan*(5/100)
                tunjanganAnak = nominalGolongan*(2/100)
        else:
            jenisKelamin = "Perempuan"
            tunjanganIstri = 0
            tunjanganAnak = 0
    else:
        tunjanganIstri = 0
        tunjanganAnak = 0

# 3. Waktu
    import time;
    
    Waktu = time.asctime( time.localtime(time.time()) )

# 4. Akhir

    print ("     SLIP GAJI          ")
    print ("     Tanggal :",Waktu,"    ")
    print ("")
    print ("Nama              :",nama)
    print ("Golongan          :",namaGolongan)
    print ("Jenis Kelamin     :",kelamin)
    print ("Status Kawin      :",statusKawin)
    print ("Gaji Pokok        :Rp. ",nominalGolongan)
    print ("Tunjangan Istri   :Rp. ",tunjanganIstri)
    print ("Tunjangan Anak    :Rp. ",tunjanganAnak)
    gajiBruto = nominalGolongan+tunjanganIstri+tunjanganAnak
    print (">> Gaji Bruto     :Rp. ",gajiBruto)
    print ("__________________________________")
    biayaJabatan = gajiBruto*(0.5/100)
    print ("Biaya Jabatan     :Rp. ",biayaJabatan)
    IuranPensiun = 15500
    print ("iuran Pensiun     :Rp. ",IuranPensiun)
    IuranOrganisasi = 3500
    print ("iuran Organisasi  :Rp. ",IuranOrganisasi)
    gajiNetto = gajiBruto-(biayaJabatan+IuranPensiun+IuranOrganisasi)
    print (">> Gaji Netto     :Rp. ",gajiNetto)
    print ("")
    print ("")
    print ("")
    


#inputan untuk break
    JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
        break