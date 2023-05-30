#if, elif, else

# nilai = int(input("masukkan nilai: "))
# if nilai >100:
#     print("nilai yang dimasukkan 0 - 100")
# elif nilai >80:
#     print("nilai A")
# elif nilai >60:
#     print("nilai B")
# elif nilai >40:
#     print("nilai C")
# elif nilai >20:
#     print("nilai D")
# elif nilai >0:
#     print("nilai E")  
# else:
#     print("nilai yang dimasukkan 0 - 100") 


#BELAJAR FUNCTION
hitung =int(input("pilih rumus yang akan dipakai:\n1.luas segitiga\n2.luas persegi\n3.luas lingkaran\n\npilih rumus: "))


def luasSegitiga():
    alas=int(input("masukkan alas: "))
    tinggi=int(input("masukkan tinggi: "))
    luas=alas*tinggi/2
    print(f"luas segitiga adalah: ",luas)

def luasPersegi():
    sisi=int(input("masukkan sisi: "))
    luas=sisi*sisi
    print(f"sisi X sisi: ",luas)

def luasLingkaran():
    r=int(input("masukkan r: "))
    luas=22/7*r*r
    print(f"luas lingkaran adalah: ",luas)       

if hitung==1:
    luasSegitiga()
elif hitung==2:
    luasPersegi()
elif hitung==3:
    luasLingkaran()










