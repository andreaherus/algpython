jawab = "y"
while jawab =="y" or jawab=="Y":
    # Menampilkan Penilaian Mahasiswa
    print ("============================")
    print (" CEK KRITERIA NILAI ")
    print ("============================")

    n = input(">> Masukkan Nilai = ")
    # Cek Kriteria Nilai 0-100
    if int(n)>0 and int(n)<=100:
        if int(n)>=91 and int(n)<=100: status="A"
        elif int(n)>=81: status="B"
        elif int(n)>=71: status="C"
        elif int(n)<71: status="D"
        print(status)
    else:
        pesan=">> Masukkan Nilai 0-100 saja"   
        print(pesan)

    # Break
    jawab = input(">> Mulai lagi ? y/t = ")
    if jawab== "t" or jawab=="T":
        break