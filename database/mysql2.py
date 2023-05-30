
import mysql.connector


#Koneksi ke database
# db = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '',
#     database = 'alpro'

# myCursor = db.cursor()


# sql = "INSERT INTO tb_matkul (b_indo, android, tbo) VALUES (%s,%s,%s)"
# data = [100,80,90]
# myCursor.execute(sql,data)
# db.commit()


        

# def mahasiswa():
#     db = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "",
#         database = "alpro"
#     )
#     myCursor = db.cursor()
#     data= []
#     nim=int(input("masukkan nim: "))
#     nama=str(input("masukkan nama: "))
#     data.append(nim)
#     data.append(nama)
#     sql="INSERT INTO tb_mahasiswa (nim,nama_mahasiswa) VALUES (%s,%s)"
#     myCursor.execute(sql,data)
#     db.commit()

# def nilai():
#     db = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "",

#         database = "alpro"
#     )
#     myCursor = db.cursor()
#     data2=[]
#     b_indo=int(input("masukkan nilai b indo: "))
#     android=int(input("masukkan nilai android: "))
#     tbo=int(input("masukkan nilai android: "))
#     data2.append(b_indo)
#     data2.append(android)
#     data2.append(tbo)
#     sql="INSERT INTO tb_matkul (b_indo,android,tbo) VALUES (%s,%s,%s)"
#     myCursor.execute(sql,data2)
#     db.commit()

# while True:
#     print("1. data mahasiswa")
#     print("2. nilai")
#     userinput = int(input("pilih satu saja: "))
#     if userinput == 1:
#         mahasiswa()
#     elif userinput == 2:
#         nilai()
#     else:
#         print("data yang anda inputkan salah")
#         break    

    



db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "alpro"
)
myCursor = db.cursor()
data2=[]
b_indo=int(input("masukkan nilai b indo: "))
android=int(input("masukkan nilai android: "))
tbo=int(input("masukkan nilai android: "))
data2.append(b_indo)
data2.append(android)
data2.append(tbo)
sql="INSERT INTO tb_matkul (b_indo,android,tbo) VALUES (%s,%s,%s)"
myCursor.execute(sql,data2)
# myCursor.execute("SELECT * FROM tb_matkul")
# myresult = myCursor.fetchall()
# for x in myresult:
#     print(x)

