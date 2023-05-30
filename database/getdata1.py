import mysql.connector
import matplotlib as plt

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_alpro'
    )
myCursor = db.cursor()
print("yes")


def insertData():
    data=[]
    nim= input("masukkan nim: ")
    name= input("masukkan nama: ")
    data.append(nim)
    data.append(name)
    # sql = "INSERT INTO datamahasiswa (nama, nim) VALUES (%s,%s)"
    myCursor.execute("INSERT INTO datamahasiswa (nim, nama) VALUES (%s,%s)",data)
    db.commit()
# insertData()

def semua_data():
    myCursor.execute("SELECT * FROM datamahasiswa")
    result = myCursor.fetchall()
    for i in result:
        print(i)
   

def tampilNamaNim():
    myCursor.execute("SELECT * FROM datamahasiswa")
    result = myCursor.fetchall()
    for i in result:
        print(i[1],i[2])

def cariDataNim():
    myCursor.execute("SELECT * FROM datamahasiswa")
    result = myCursor.fetchall()
    cariNim=input("masukkan nim untuk melihat data: ")
    for i in result:
        if i [1] ==cariNim:
            print(i)

def tambahNilai():
    data2=[]
    bahasa=int(input("masukkan nilai bahasa: "))
    agama=int(input("masukkan nilai agama: "))
    alpro=int(input("masukkan nilai alpro: "))
    data2.append(bahasa)
    data2.append(agama)
    data2.append(alpro)
    sql="INSERT INTO tb_nilai (bahasa,agama,alpro) VALUES (%s,%s,%s)"
    myCursor.execute(sql,data2)
    db.commit()

def grafik():
    sql="SELECT * FROM tb_nilai"
    myCursor.execute(sql)
    result = myCursor.fetchone()
    nama = ["bahasa", "agama", "alpro"]
    print(result)
    plt.bar(nama,result[1:])
    plt.show()



while True:
    print("1. insert data")
    print("2. tampilkan semua data")
    print("3. tampilkan nama, nim")
    print("4. cari data berdasarkan nim")
    print("5. tambahkan nilai")
    print("6. tampilan grafik")
    print("5. exit")
    pilih =input("pilih menu: ")
    if pilih =="1":
        insertData()
    elif pilih =="2":
        semua_data() 
    elif pilih =="3":
        tampilNamaNim()
    elif pilih =="4":
        cariDataNim()
    elif pilih =="5":
        tambahNilai()
    elif pilih =="6":
        grafik()
    else:
        break
        print("terima kasih")