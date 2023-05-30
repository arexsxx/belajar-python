import mysql.connector

#Koneksi ke database
db = mysql.connector.connect(
    host = 'localhost', #atau '127.0.0.1'
    user = 'root',
    password = '',
    database = 'karyawan'
    )

def masuk():
    a = db.cursor()
    b = "INSERT INTO kr (kode,nama,jenis,sandi,gaji) VALUES(%s,%s,%s,%s,%s)"
    c = input("Masukkan kode karyawan:")
    d = input("Masukkan nama karyawan:")
    e = input("Masukkan jenis karyawan:")
    g = input("Masukkan sandi karyawan:")
    h = input("Masukkan Gaji karyawan:")
    f = (c,d,e,g,h)
    a.execute(b,f)
    db.commit()
    print("Sukses")



def semua():
    a = db.cursor()
    a.execute("SELECT kode,nama,jenis FROM kr")
    b = a.fetchall()
    for i in range(len(b)):
            print(f"Kode Karyawan         : {b[i][0]}")
            print(f"Nama Karyawan         : {b[i][1]}")
            print(f"Jenis Karyawan        : {b[i][2]}")
            print('='*20)
        
    print('{} data berhasil ditampilkan'.format(a.rowcount))

def cari():
    a = db.cursor()
    b = "SELECT kode,nama,jenis FROM kr"
    c = input("Masukkan kode karyawan:")
    a.execute(b)
    d = a.fetchall()
    for i in d:
        if i[0] == c:
            print('='*20)
            print(f"Kode Karyawan       : {i[0]}")
            print(f"Nama Karyawan       : {i[1]}")
            print(f"Jenis Karyawan      : {i[2]}")
            print('='*20)

    print('data berhasil ditampilkan'.format(a.rowcount))
  



while True:
    print("="*20)
    print("1.Login sebagai Admin")
    print("2.Login sebagai Karyawan")
    print("3.Keluar")
    print("="*20)
    a = int(input("Masukkan pilihan login:"))
    if a == 1:
            b = input("Masukkan sandi:")
            if b == "a":
                while True:
                    print("="*20)
                    print("1.Input data karyawan")
                    print("2.Lihat Data semua karyawan")
                    print("3.Cari Karyawan")
                    print("4.keluar")
                    print("="*20)
                    c = int(input("Masukkan pilihan :"))
                    if c == 1:
                        masuk()
                    elif c == 2:
                        semua()
                    elif c == 3:
                        cari()
                    elif c == 4:
                        break
    elif a == 2 :
            c = db.cursor()
            c.execute("SELECT * FROM kr")
            e = c.fetchall()
            # print(e)
            a = input("Masukkan username:")
            b = input("Masukkan password:")    
            for i in e:
                if a == i[1] and b == i[3] :
                    print("Mantabb")
                    while True:
                        print("="*20)
                        print("1.Lihat Gaji")
                        print("2.Lembur")
                        print("3.Keluar")
                        print("="*20)
                        a = int(input("Masukkan pilihan:"))
                        if a == 1:
                            print(f"Gaji pokok adalah {i[4]}")
                        elif a == 2:
                            b = int(input("Masukkan jam lembur:"))
                            c = b *10000
                            d = c + i[4]
                            print(f"Total gaji ditambah lembur {d}")
                        elif a == 3:
                            break



    elif a == 3:
        break