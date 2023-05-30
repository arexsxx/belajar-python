#Fungsi atau sub program atau method atau sub routine

#default penulisan fungsi:
# def namaFungsi():
#     badan fungsi

# def print_nama():
#     print("nama saya adalah paijo")


    
 # #contoh 2
# def luas_persegi():
#     sisi = 10
#     luas = sisi*sisi
#     print("luas persegi adalah {luas}") 
    
# luas_persegi()    
    
#contoh 3
# def luasPersegiInput():
#     sisi = int(input("masukkan panjang sisi: "))
#     luas = sisi * sisi
#     print(f"luas persegi adalah {luas}")
    
# luasPersegiInput()  


#fungsi menggunakan parameter / argument
# def luasSegitiga(alas, tinggi):
#     luas = alas * tinggi / 2
#     print(f"luas persegi adalah {luas}")


#Fungsi menggunakan return
# def persegi(sisi):
#     luas = sisi * sisi    
#     return luas


# tampung = 20 + persegi(10) 
# print(tampung)

# def kalkulator(angka_satu, angka_dua):
#     tambah = angka_satu + angka_dua
#     kali = angka_satu * angka_dua
#     kurang = angka_satu - angka_dua
#     return tambah, kurang, kali

# a,b,c = kalkulator(10, 5)
# lanjutan = +10
# print(a)
# print(b)
# print(c)
    
       
#Default parameter atau argumen
# def tambah(angka1=10, angka2=5, angka3=15):
#     proses = angka1 + angka2 + angka3
#     print("hasilnya adalah", proses)
    
# tambah(angka3=10, angka1= 20)


#kuis
print("masukkan pilihan rumus:\n1.luas segitiga\n2.luas persegi\n3.luas lingkaran")

hitung=int(input("pilihan rumus:"))

def luasSegitiga():
    alas=int(input("masukkan alas:"))
    tinggi=int(input("masukkan tinggi:"))
    luas=alas*tinggi /2
    print(f"luas segitiga:{luas}")
    
def luasPersegi():
    sisi=int(input("masukkan sisi:"))
    luas=sisi *sisi
    print(f"luas persegi:{luas}")
    
def luasLingkaran():
    r=int(input("masukkan r:"))
    luas=22/7*r*r
    print(f"luas lingkaran:{luas}")    
    
if hitung==1:
    luasSegitiga()
elif hitung==2:
    luasPersegi()
elif hitung==3:
    luasLingkaran()    


