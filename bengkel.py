"""
Created on Thu Jun 18 16:10:05 2021

@author: Andrea
"""
JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print("==================================================")
    print(" TRANSAKSI PEMBELIAN OLI UD. Matahari ")
    print("==================================================")
    print(" a = Duration SW20 1L @ Rp53.000")
    print(" b = Castrol Magnatec 1L @ Rp50.000")
    print(" c = Federal Supreme XX 1L @ Rp54.000")
    print(" d = Yamalube 1L @ Rp45.000")
    print(" e = Shell 1L @ Rp46.000")
    print(" ")
    print(" ")
    print(" ")
#jika menggunakan list Kode dibawah ini, maka metode yang digunakanadalah mendeteksi indeks value yang terpilih pada list kode. caranya: melakukan pencarian pada list kode menggunakan 
# nilai kode yang diinputkan
    kode =['a','b','c','d','e']

    namaBarang = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
    harga = [53000,50000,54000,45000,46000]

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
            if jumlah >=200000:
                diskon = jumlah*(5/100)
                ppn = jumlah*(1/100)
                print(">>> Total        = Rp. "+ str(jumlah))
                print(">>> Diskon 5%    = Rp. "+ str(diskon))
                print(">>> PPN 1%       = Rp. "+ str(ppn))
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
                ppn = jumlah*(1/100)
                print(">>> Total        = Rp. "+ str(jumlah))
                print(">>> PPN 1%       = Rp. "+ str(ppn))
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