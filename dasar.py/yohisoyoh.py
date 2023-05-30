def hitung_kecepatan():
    print("hitung kecepatan siap\n")
    jarak = int(input("masukkan jarak: "))
    waktu = int(input("masukkan waktu: "))
    kecepatan = jarak * waktu
    print("kecepatan", kecepatan, "\n")

def luas_segitiga():
    print("hitung luas segitiga")
    alas = int(input("masukkan alas: "))
    tinggi = int(input("masukkan tinggi: "))
    luas = alas * tinggi / 2
    print("luas", luas, "\n")

def luas_balok():
    print("hitung luas balok")
    panjang = int(input("masukkan panjang: "))
    lebar = int(input("masukkan lebar: "))
    tinggi = int(input("masukkan tinggi: "))
    luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
    print("luas balok adalah", luas, "\n")

def luas_trapesium():
    print("hitung luas trapesium")
    a = int(input("masukkan a: "))
    b = int(input("masukkan b: "))
    tinggi = int(input("masukkan tinggi: "))
    luas = (a + b) * tinggi / 2
    print("luas trapesium adalah", luas, "\n")    

while True:
    userinput = int(input("pilih rumus yg akan dipakai: \n\n1.hitung rumus kecepatan\n2.luas segitiga\n3.luas balok\n4.luas trapesium\n\n0.keluar program\n\npilih nomer berapa: "))
    if(userinput == 1):
        hitung_kecepatan()
    elif(userinput ==2):
        luas_segitiga()
    elif(userinput ==3):
        luas_balok()
    elif(userinput ==4):
        luas_trapesium()    


    else:
        break        






