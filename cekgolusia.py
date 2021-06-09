jawab = "y"
while jawab =="y" or jawab=="Y":

    # Cek Golongan Usia
    print ("============================")
    print (" CEK GOLONGAN USIA ")
    print ("============================")

    u = input(">> Masukkan Usia = ")
    # Cek Usia - batas inputan usia 0-100
    if int(u)>0 and int(u)<=100:
        if int(u)>=60: status="Lansia"
        elif int(u)>=35: status="Dewasa"
        elif int(u)>=18: status="Pemuda"
        elif int(u)>=15: status="Remaja"
        elif int(u)<15: status="Anak"
        print(status)
    else:
        pesan=">> Masukkan Angka Usia 0-100 saja"   
        print(pesan)

    # Break
    jawab = input(">> Mulai lagi ? y/t = ")
    if jawab== "t" or jawab=="T":
        break