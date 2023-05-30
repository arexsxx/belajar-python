import mysql.connector
import matplotlib.pyplot as plt

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_kuliah'
)

myCursor = db.cursor()

def menuAdmin():
    print("menu admin:")
    print("1. input data")
    print("2. get semua data kecuali id")
    print("3. cari data berdasar nim atau nama")

def inputData():
    data=[]
    nim=input("masukkan nim: ")
    nama=input("masukkan nama: ")
    nilaiAl=input("masukkan nilai alpro: ")
    nilaiAg=input("masukkan nilai agama: ")
    nilaiTbo=input("masukkan nilai tbo: ")
    data.append(nim)
    data.append(nama)
    data.append(nilaiAg)
    data.append(nilaiAl)
    data.append(nilaiTbo)
    sql = "INSERT INTO tb_mahasiswa (nim, nama, nilai_alpro, nilai_agama, nilai_tbo) VALUES (%s,%s,%s,%s,%s)"
    myCursor.execute(sql,data)
    db.commit()

def getData():
    myCursor.execute("SELECT * FROM tb_mahasiswa")
    result = myCursor.fetchall()
    for i in result:
        print("nim: ",i[1])
        print("nama: ",i[2])
        print("nilai alpro: ",i[3])
        print("nilai agama: ",i[4])
        print("nilai tbo: ",i[5])
        print("="*10)

def cariData():
    myCursor.execute("SELECT * FROM tb_mahasiswa")
    result=myCursor.fetchall()
    npm=input("masukkan nim: ")
    for i in result:
        if i [1]== npm:
            print(i)

def grafik():
    myCursor.execute("SELECT * FROM tb_mahasiswa")
    result = myCursor.fetchall()
    nim = input("Masukan NIM : ")
    for i in result:
        if i[1] == nim:
            myCursor.execute("SELECT * FROM tb_matkul")
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




while True:
    print("pilih user: ")
    print("1. menu admin ")
    print("2. menu mahasiswa ")
    pilih=input("silahkan pilih: ")
    if pilih =="1":
        pw=input("masukkan password: ")
        if pw =="admin123":
            menuAdmin()
            pilihMn=input("pilih menu: ")
            if pilihMn=="1":
                inputData()
                ulang=input("apakah anda ingin input lagi? y/t: ")
                if ulang=="t":
                    menuAdmin()

                elif ulang=="y":
                    inputData()

            elif pilihMn=="2":
                getData()
            elif pilihMn=="3":
                cariData()
            else:
                 print("password yang anda masukkan salah")
                 break
    elif pilih=="2":
        print("menu mahasiswa: ")
        print("1. lihat data berdasarkan nim")
        print("2. tampilkan grafik")
        mlh=input("pilih salah satu: ")
        if mlh=="1":
            cariData()
        elif mlh=="2":
            grafik()
        else:
            print("data yang anda masukkan tidak ditemukan")

        











