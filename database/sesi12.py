import mysql.connector
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_perusahaan'
)

myCursor = db.cursor()

def inputNama():
    data=[]
    kode=input("masukkan kode: ")
    nama=input("masukkan nama: ")
    jenisKar=input("masukkan Jenis Karyawan: ")
    data.append(kode)
    data.append(nama)
    data.append(jenisKar)
    sql = "INSERT INTO tb_admin (kode_karyawan, nama_karyawan, jenis_karyawan) VALUES (%s,%s,%s)"
    myCursor.execute(sql,data)
    db.commit()

def liatSemuaData():
    myCursor.execute("SELECT * FROM tb_admin")
    result = myCursor.fetchall()
    for i in result:
        print("kode karyawan: ",i[1])
        print("nama karyawan: ",i[2])
        print("jenis karyawan: ",i[3])
        print("="*10)

def cari():
    myCursor.execute("SELECT * FROM tb_admin")
    result=myCursor.fetchall()
    print("1. Cari Berdasarkan kode karyawan ")
    print("2. Cari Bersarkan Nama karyawan")
    pilih = input("Pilih Menu : ")
    if pilih=="1":
        kode = input("masukkan kode karyawan: ")
        for i in result:
            if i[1]== kode:
                print("kode karyawan: ",i[1])
                print("nama karyawan: ",i[2])
                print("jenis karyawan: ",i[3])
                print("="*10)
                break
                
            else:
                print("data tidak ada")
    elif pilih=="2":
        nama = input("masukkan nama karyawan: ")
        for i in result:
            if i[2]== nama:
                print("kode karyawan: ",i[1])
                print("nama karyawan: ",i[2])
                print("jenis karyawan: ",i[3])
                print("="*10)
                break
         
            else:
                print("data tidak ada")
    
def admin():
        pw=input("masukkan password: ")
        if pw=="halo123":
            while True:  
                print("1. Input data karyawan: ")
                print("2. lihat semua data karyawan: ")
                print("3. cari karyawan: ")
                pilih=input("pilih menu: ")
                if pilih=="1":
                        inputNama()
                elif pilih=="2":
                        liatSemuaData()
                elif pilih=="3":
                        cari()
        else:
             print("password yang anda masukkan salah")

     
while True:
    print("menu")
    print("1. menu admin")
    print("2. menu karyawan")
    pilih=input("pilihn menu: ")
    if pilih=="1":
        admin()
    elif pilih=="2":
         break

    

     






