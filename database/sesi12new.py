import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'perusahaan'
)
myCursor = db.cursor()

def inputData():
    kode=input("masukkan kode karyawan: ")
    name=input("masukkan nama karyawan: ")
    jenis=input("masukkan jenis karyawan: ")
    sandi=input("masukkan sandi karyawan: ")
    gaji=input("masukkan gaji karyawan: ")
    data=(kode,name,jenis,sandi,gaji)
    sql= "INSERT INTO admin (kode_karyawan,namaKaryawan,jenisKaryawan,sandi,gaji) VALUES(%s,%s,%s,%s,%s)"
    myCursor.execute(sql,data)
    db.commit()

def lihatdata():
    myCursor.execute("SELECT kode_karyawan,namaKaryawan,jenisKaryawan FROM admin")
    result = myCursor.fetchall()
    for i in result:
        print("kode karyawan     :",i[0])
        print("nama karyawan     :",i[1])
        print("jenis karyawan    :",i[2])
        print("="*20)

def cari():
    myCursor.execute("SELECT kode_karyawan, namaKaryawan, jenisKaryawan FROM admin")
    result= myCursor.fetchall()
    a = input("masukkan kode karyawan: ")
    for i in result:
        if i[0] == a:
            print("="*20)
            print(f"kode karyawan     :{i[0]}")
            print(f"nama karyawan     :{i[1]}")
            print(f"jenis karyawan     :{i[2]}")
            print("="*20)

            print('data berhasil ditampilkan')

def plot():
    myCursor.execute("SELECT kode_karyawan, namaKaryawan, jenisKaryawan FROM admin")
    result= myCursor.fetchall()
    for i in result:
        print(i[2])
        if i[2] == "progammer":
            programmer =+1
            plt.bar(["programmer"],programmer)

        elif i[2] == 'manager':
            manager =+3
            plt.bar(["manager"],manager)

        elif i[2] == 'office boy':
            office_boy =+1
            plt.bar(["office_boy"],office_boy)

        elif i[2] == 'direktur':
            direktur =+4
            plt.bar(["direktur"],direktur)    
    plt.show()


while True:
    print("menu")
    print("="*27)
    print("1. menu admin")
    print("2. menu karyawan")
    print("3. exit")
    pilih=int(input("pilih menu: "))

    if pilih == 1:
        pw=input("masukkan sandi: ")
        if pw == "123":
            while True:
                print("="*20)
                print("1. input data karyawan")
                print("2. tampilkan semua data")
                print("3. cari data karyawan")
                print("4. Tampil plotbar")
                print("5. exit")
                print("="*20)
                pil=int(input("pilih menu admin: "))
                if pil == 1:
                    inputData()
                elif pil == 2:
                    lihatdata()
                elif pil == 3:
                    cari()
                elif pil == 4:
                    plot()
                    break
                elif pil == 5:
                    break
        else :
                print("sandi yang anda masukkan salah :( \nulangi lagi")
            
    elif pilih == 2:
        myCursor.execute("SELECT * FROM admin")
        result= myCursor.fetchall()
        user=input("masukkan username : ")
        sandi=input("masukkan password: ")
        for i in result:
            if user == i[1] and sandi == i[3]:
                print("login sukses")
                while True:
                    print("1. lihat gaji")
                    print("2. waktu lembur(jam)")
                    print("3. exit")
                    p=int(input("pilih menu: "))
                    if p == 1:
                        print(f"gaji pokok   : {i[4]}")
                    elif p == 2:
                        lembur= int(input("masukkan waktu lembur: "))
                        jumlah= lembur*10000
                        total= jumlah + i[4]
                        print(f"total gaji pokok ditambah lembur {total}")
                    elif p == 3:
                        break
            else:
                print('KATA SANDI SALAH')

    elif pilih == 3:
        print("BERHASIL LOG OUT")
        break