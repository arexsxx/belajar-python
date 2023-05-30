import mysql.connector
import matplotlib.pyplot as plt




db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_mahasiswa'
)

cursor = db.cursor()
print("berhasil")

def tb_data():
    data = []
    iNama = input('masukkan nama lengkap: ')
    iNIM = input("masukkan NIM: ")
    data.append(iNama)
    data.append(iNIM)
    # sql = "INSERT INTO tb_data(nama,nim)VALUE(%s,%s)"
    cursor.execute("INSERT INTO tb_data(nama,nim)VALUE(%s,%s)",data)
    db.commit()
    print("data berhasil di inputkan")

def tb_mahasiswa():
    data = []
    while True:
        input_nilai = input("masukkan nilai: ")
        data.append(input_nilai)
        ulang = input("apakah ingin mengisi nilai lagi? y/t: ")
        if ulang == "y":
            print(data)
            continue
        elif ulang == "t":
            break
        elif input_nilai == "c":
            break
        else:
            print("angka yang anda masukkan salah, program diulang")
            exit()
    cursor.execute("INSERT INTO tb_mahasiswa(bahasa, agama, alpro) VALUE(%s,%s,%s)")
    db.commit()
    print("succesful insert into tb_mahasiswa")

def tampil_data():
    cursor.execute("SELECT * FROM tb_data")
    result = cursor.fetchall()
    for i in result:
        print(i)

def tampil_data_nim():
    cursor.execute("SELECT * FROM tb_data")
    result = cursor.fetchall()
    for i in result:
        print(i[1])

def cari_data():
    # cursor = db.cursor()
    # db.commit()
    cursor.execute("SELECT * FROM tb_data")
    result = cursor.fetchall()
    cari = input("cari: ")
    for i in result:
        if i[1] == cari:
            print(i)

def grafik():
    sql = "SELECT * FROM tb_mahasiswa"
    cursor.execute(sql)
    result = cursor.fetchone()
    nama = ["bahasa","agama","alpro"]
    print(result)
    plt.bar(nama, result[1:])
    plt.show()


while True:
    print("="*28)
    print("="*10 + "DATABASE" + "="*10)
    print("MENU")
    print("a.input data")
    print("b.tampilkan semua data")
    print("c.tampilkan data berdasarknan nim")
    print("d.cari data berdasarknan nim")
    print("e.grafik nilai")
    print("f.exit")
    menu = input("masukkan pilihan a-e: ")
    if menu == "a":
        tb_data()
    elif menu == "b":
        tampil_data()
    elif menu == "c":
        tampil_data_nim()
    elif menu == "d":
        cari_data()
    elif menu == "e":
        grafik()
    else:
        print("\n\nMASUKKAN ANGKA YANG SESUAI...\n\n")
        continue