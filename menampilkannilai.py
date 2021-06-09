jawab = "y"
while jawab =="y" or jawab=="Y":

    # Menampilkan Nilai Huruf
    print ("============================")
    print (" CEK GOLONGAN NILAI ")
    print ("============================")

    n = input(">> Masukkan Nilai = ")
    # Cek Nilai Bilangan Bulat 0-100
    if int(n)>0 and int(n)<=100:
        if int(n)>=80: status="BAIK SEKALI"
        elif int(n)>=65: status="BAIK"
        elif int(n)>=55: status="CUKUP"
        elif int(n)>=40: status="KURANG"
        elif int(n)<=40: status="KURANG SEKALI"
        print(status)
    else:
        pesan=">> Masukkan Nilai Bulangan Bulat 0-100 saja"   
        print(pesan)


     # Break
    jawab = input(">> Mulai lagi ? y/t = ")
    if jawab== "t" or jawab=="T":
        break