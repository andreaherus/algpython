"""
Created on Thu Jun 18 16:30:12 2021

@author: Andrea
"""
JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print("==================================================")
    print(" TRANSAKSI PEMBELIAN UD. Subur ")
    print("==================================================")
    print(" a = Asbes Gelombang @ Rp60.000")
    print(" b = Cat Tembok Dulux 1Galon @ Rp250.000")
    print(" c = Cat Tembok Avian 1 Galon @ Rp350.000")
    print(" d = Aquaproof 5 Kg @ Rp50.000")
    print(" e = Seng 2mm @ Rp70.000")
    print(" f = Spandeks 1mm @ Rp92.000")
    print(" ")
    print(" ")
    print(" ")
#jika menggunakan list Kode dibawah ini, maka metode yang digunakanadalah mendeteksi indeks value yang terpilih pada list kode. caranya: melakukan pencarian pada list kode menggunakan 
# nilai kode yang diinputkan
    kode =['a','b','c','d','e','f']

    namaBarang = ['Asbes Gelombang','Cat Tembok Dulux 1Galon','Cat Tembok Avian 1 Galon','Aquaproof 5 Kg','Seng 2mm','Spandeks 1mm']
    harga = [60000,250000,350000,50000,70000,92000]

    pilihan = input(">> Masukkan Kode Barang = ")
    qty = input(">> Masukkan Qty. Barang yang akan di beli =")
    print(" ")
    print(" ")

    #identifikasi Indeks list berdasarkan pilihan
    # baca berulang2 index dalam list kode, jika value sama dengan value pilihan, ambil index nya dengan metode while
    index = 0
    while index < len(kode):
        if kode[index] == pilihan:
            print ("*********** RINCIAN PEMBELIAN *************")
            print(">>> Nama Barang      = " + namaBarang[index ])
            print(">>> Harga Barang     = Rp. " + str(harga[index]))
            print(">>> Qty. Barang      = "+ str(qty)+" bh")
            print("================================================")
#tahap hitung biaya
            jumlah = harga[index] * int(qty)
            if jumlah >=500000:
                diskon = jumlah*(5/100)
                ppn = jumlah*(2/100)
                print(">>> Total        = Rp. "+ str(jumlah))
                print(">>> Diskon 5%    = Rp. "+ str(diskon))
                print(">>> PPN 2%       = Rp. "+ str(ppn))
                print("================================================")
#tampilkan total bayar
                print(">>>> Total Bayar = Rp. " + str((jumlah + ppn) - diskon))
                print(" ")
                print("================================================")
                print(" ")
                print(" ")
                print(" ")

            else:
                jumlah = harga[index] * int(qty)
                ppn = jumlah*(2/100)
                print(">>> Total        = Rp. "+ str(jumlah))
                print(">>> PPN 2%       = Rp. "+ str(ppn))
                print("================================================")
#tampilkan total bayar
                print(">>>> Total Bayar = Rp. " + str(jumlah + ppn))
                print(" ")
                print("================================================")
                print(" ")
                print(" ")
                print(" ")
                
	#fungsi index + 1 adalah misal anda memlilih kode b maka akan dibaca index 0+1=1 jadi kode b ada index ke 1, dst
        index = index + 1 
        
#inputan untuk break
    JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
        break