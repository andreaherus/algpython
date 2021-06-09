jawab = "y"
while jawab =="y" or jawab=="Y":

    #cek kelulusan, jika nilai >60 maka status lulus
    print ("============================")
    print (" CEK KELULUSAN ")
    print ("============================")

    n = input(">> Masukkan Nilai = ")
    # Cek Nilai
    if int(n)>60:
        status = "LULUS"
    else:
        status = "TIDAK LULUS"

    print(status)

    
     # Break
    jawab = input(">> Mulai lagi ? y/t = ")
    if jawab== "t" or jawab=="T":
        break