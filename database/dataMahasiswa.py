import mysql.connector
import matplotlib.pyplot as plt

db = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "",
    database = "mahasiswa"
)
myCursor=db.cursor()

def inputData():
    a = "INSERT INTO tb_mahasiswa (nim,nama,prodi,jenisKelamin) VALUES(%s,%s,%s,%s)"
    nim = input("masukkan nim :")
    nama = input("masukkan nama :")
    prodi = input("masukkan prodi :")
    jenisKelamin = input("masukkan jenis kelamin :")
    data=(nim,nama,prodi,jenisKelamin)
    myCursor.execute(a,data)
    db.commit()

def lihatData():
    myCursor.execute("SELECT * FROM tb_mahasiswa")
    result=myCursor.fetchall()
    for i in result:
        print("="*10)
        print(f"nim  :",i[0])
        print(f"nama :",i[1])
        print(f"prodi:",i[3])
        print("_"*10)

def lihatDataNim():
    myCursor.execute("SELECT * FROM tb_mahasiswa")
    result = myCursor.fetchall()
    a = int(input("masukkan nim: "))
    for i in result:
        if i[0] == a:
            print("="*10)
            print(f"nim                  :",i[0])
            print(f"nama                 :",i[1])
            print(f"prodi                :",i[2])
            print(f"jenis kelamin        :",i[3])
            print("="*10)
#Tampilkan grafik cara ruwet

# def grafik():
#     myCursor.execute("SELECT * FROM tb_mahasiswa")
#     result = myCursor.fetchall()
#     data = []
#     hukum = []
#     Si = []
#     If = []
#     for i in result:
#         print(i)
#         if i[2] == "hukum":
#             hukum.append("1")
#         elif i[2] == "sistem informasi":
#             Si.append("1")
#         elif i[2] == "informatika":
#             If.append("1")
#     data.append(len(hukum))        
#     data.append(len(Si))        
#     data.append(len(If))        
#     x = ["hukum","sistem informasi","informatika"]
#     plt.bar(x,data)
#     plt.show()  

#Tampil grafik cara simple
def grap():
    myCursor.execute("SELECT prodi,COUNT(prodi) FROM tb_mahasiswa  GROUP BY prodi") 
    result = myCursor.fetchall()   
    for i in result:
        plt.bar(i[0],i[1])
    plt.show()



def dataMhsw():
    myCursor.execute("SELECT * FROM tb_mahasiwa")
    result = myCursor.fetchall()
    a = int(input("masukkan nim: "))
    for i in result:
        if i[0] == a:
            print("="*10)
            print(f"nim                  :",i[0])
            print(f"nama                 :",i[1])
            print(f"prodi                :",i[2])
            print(f"jenis kelamin        :",i[3])
            print("="*10)


def user():
    psw = input("masukkan password : ")
    if psw == "123":
        print("="*3,"Menu User","="*3)
        print("1. Lihat data  semua mahasiswa")
        print("2. Lihat Data Berdasarkan Nim")
        print("3. Tampilkan grafik")
        print("4. Exit")
        pil = input("pilih menu")
        if pil == "1":
            dataMhsw()







while True:
    print("="*5,"menu","="*5)
    print("1. admin")
    print("2. user")
    print("3. keluar")
    pilih=input("Pilih Menu    : ")
    if pilih == "1":
        pw=input("masukkan password : ")
        if pw == "admin123":
            while True:
                print("="*3,"Menu Admin","="*3)
                print("1. Input Data")
                print("2. Lihat Semua Data")
                print("3. Lihat Data Berdasarkan Nim")
                print("4. Tampilkan grafik")
                print("5. Exit")
                pilih=input("pilih menu    : ")
                if pilih == "1":
                    inputData()
                    ulang=input("apakah ingin input lagi? y/t  : ")
                    if ulang == "y":
                        inputData()
                    elif ulang == "t":
                        break
                elif pilih == "2":
                    lihatData()
                elif pilih == "3":
                    lihatDataNim()
                elif pilih == "4":
                    grap()    
                elif pilih == "5":
                    break
    elif pilih == "2":
        user()     
                   



    
