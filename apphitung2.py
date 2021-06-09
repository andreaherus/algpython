jawab = "y"
while jawab =="y" or jawab=="Y":

    # Hitung Nilai Transaksi
    print ("============================")
    print (" TRANSAKSI PEMBELIAN PRINTER ")
    print ("============================\n")


    # Data Printer
    NamaBarang = "Printer Epson T20"
    HargaPrint = 660000


    # Daftar barang
    print ("*****************************")
    print (" DAFTAR BARANG ")
    print ("*****************************")
    print ("1. " + NamaBarang + " (Rp. "+ str(HargaPrint) + ",-)\n" )
    print ("\n")




    # Input Transaksi
    QtyBeli = input("Masukkan Qty."+ NamaBarang +" yang akan dibeli = ")
    print ("\n")


    # Proses Hitung
    Jumlah = HargaPrint*int(QtyBeli)

    t = Jumlah
    # Cek Nominal Pembelian
    if int(t)>1500000 :
        # Tampilkan Hasil Grosir
        print ("******* RINCIAN PEMBELIAN ************")
        print (NamaBarang + "  |  " + str(HargaPrint) + " X " + QtyBeli + " buah")
        print ("Jumlah " + str(t))
        print ("Diskon 15% = Rp. " + str(t * 15/100) )
        print ("-------------------------------------")
        print ("Total Transaksi Pembelian Printer "+ NamaBarang + "  Rp. " + str(t-(t*15/100)) + ",-\n" )
        

    else:
        # Tampilkan Hasil Satuan
        print ("******* RINCIAN PEMBELIAN ************")
        print (NamaBarang + "  |  " + str(HargaPrint) + " X " + QtyBeli + " buah")
        print ("Jumlah " + str(t))
        print ("Diskon 15% = Rp. 0" )
        print ("-------------------------------------")
        print ("Total Transaksi Pembelian Printer "+ NamaBarang + "  Rp. " + str(t) + ",-\n" )


    # Break
    jawab = input(">> Mulai lagi ? y/t = ")
    if jawab== "t" or jawab=="T":
        break
