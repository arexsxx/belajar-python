import mysql.connector
import matplotlib.pyplot as plt

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'kuliah'
)

myCursor = db.cursor()

def inputData():
    data=[]
    nim=input("masukkan nim: ")
    nama=input("masukkan nama: ")
    nilaiAg=input("masukkan nilai agama: ")
    nilaiAl=input("masukkan nilai alpro: ")
    nilaiAp=input("masukkan nilai apti: ")
    data.append(nim)
    data.append(nama)
    data.append(nilaiAg)
    data.append(nilaiAl)
    data.append(nilaiAp)
    sql="INSERT INTO tb_mahasiswa(nim,nama,nilai_agama,nilai_alpro,nilai_apti) VALUES (%s,%s,%s,%s,%s)"
    myCursor.execute(sql,data)
    db.commit()

def semuaData():
    myCursor.execute("SELECT * FROM tb_mahasiswa")
    result=myCursor.fetchall()
    for i in result:
        print("nim: ",i[1])
        print("nama: ",i[2])
        print("nilai agama: ",i[3])
        print("nilai alpro: ",i[4])
        print("nilai apti: ",i[5])
        print("="*10)

def cariData():
    myCursor.execute("SELECT * FROM tb_mahasiswa")
    result=myCursor.fetchall()
    print("1. cari data berdasarkan nim: ")
    print("2. cari data berdasarkan nama: ")
    pilih=input("pilih menu: ")
    if pilih=="1":
        nim=input("masukkan nim: ")
        for i in  result:
            if i [1]== nim:
                print("nim: ",i[1])
                print("nama: ",i[2])
                print("nilai agama: ",i[3])
                print("nilai alpro: ",i[4])
                print("nilai apti: ",i[5])
                print("="*10)
                break
            else:
                print("data tidak ada")
    elif pilih=="2":
        nama=input("masukkan nama: ")
        for i in result:
            if i[2] == nama:
                print("nim: ",i[1])
                print("nama: ",i[2])
                print("nilai agama: ",i[3])
                print("nilai alpro: ",i[4])
                print("nilai apti: ",i[5])
                print("="*10)
                break
            else:
                print("data tidak ada")

def admin():
    pw=input("masukkan password: ")
    if pw != "admin123":
        print("password salah")
        return True
    else:
        while True:
            print("1.Input Data ")
            print("2.Tampil Semua Data")
            print("3.Cari Data")
            print("4.Kembali ke Menu awal")
            pilih=input("pilih menu: ")
            if pilih =="1":
                inputData()
            elif pilih =="2":
                semuaData()
            elif pilih =="3":
                cariData()
            elif pilih =="4":
                print("kembali ke menu awal")
                return True

def dataMahasiswa():
    myCursor.execute("SELECT * FROM tb_mahasiswa")
    result=myCursor.fetchall()
    nim=input("masukkan nim: ")
    for i in  result:
        if i [1]== nim:
            print("nim: ",i[1])
            print("nama: ",i[2])
            print("nilai agama: ",i[3])
            print("nilai alpro: ",i[4])
            print("nilai apti: ",i[5])
            print("="*10)
            break
        else:
            print("data tidak ada")

def grafik():
    myCursor.execute("SELECT * FROM tb_mahasiswa")
    result = myCursor.fetchall()
    nim = input("Masukan NIM : ")
    for i in result:
        if i[1] == nim:
            myCursor.execute("SELECT * FROM matkul")
            data = myCursor.fetchone()
            nama = []
            nama.append(data[1])
            nama.append(data[2])
            nama.append(data[3])
            nilai = i[3:]
            plt.bar(nama,nilai)
            plt.show()
        else:
            print("Data Tidak Ada")

def mahasiswa():
     while True:
        print("1. Lihat Data Berdasarkan NIM")
        print("2. Tampilkan Grafik Nilai")
        print("3. Kembali")
        pilih = input("Pilih Menu : ")
        if pilih == "1":
           dataMahasiswa()
        elif pilih == "2":
            grafik()
        elif pilih == "3":
            print("Kembali")
            return True
        else:
            print("Menu tidak Ada")



while True:
    print("pilih menu: ")
    print("1. menu admin")
    print("2. menu mahasiswa")
    print("3. exit")
    pilih = input("pilih menu: ")
    if pilih =="1":
        admin()
    elif pilih =="2":
        mahasiswa()
    else:
        print("anda telah keluar dari program")
        break    
        
                



