##Tipe data lanjut
#Tipe data List  ( penulisannya menggunakan kurung siku[] )

dataListNama = ["Mizard","Jamal","Udin"]
dataListAngka = [10,20,30,40,50]
dataListFloat = [10.20, 10.5, 11.5]
dataListbool = [True, False, False, True]
dataListMix = [10, 'mizard', True, 20.5]
#print(daraListNama)

#Tipe Data Distionary (berisikan key dan value)
dic = {
    "nama"  : "mizard",
    "kelas" : 10,
    "tampan": True,
    "berat" : 57.5,
    "list"  : ['jamal', 'udin', 'samsudin']
}
print(dic['kelas'])

#Tipe data tuple (menggunakan kurung biasa() ) tidak bisa dirubah
dataTuple = ('mizard', 'jamal', 'udin')
dataMix = ('mizard', 10, True, 20.5)
#print(dataMix)

#Tipe data Set {}
dataSet = {'mizard', 'jamal', 'udin'}
#print(dataSet)


#Casting data = Merubah tipe data ke tipe data lainnya

dataString  = '140'
ubahInteger = int(dataString) 
ubahFloat   = float(dataString)
#print("ini diubah ke integer", ubahInteger)
#print("ini diubah ke float", ubahFloat)

dataInt = 10
ubahString = str(dataInt)
ubahFloat   = float(ubahInteger)
#print("ini diubah ke string", str(dataInt))
#print("ini diubah ke float", float(dataInt))

##inputan 
tinggi = input("masukan tinggi :")
userFloat = float(input("masukan tinggi :"))
userInt = int(input("masukan tinggi :"))


sisi = input("masukan sisi :",)
ubahinterger = int(sisi)
Luas = int(sisi)*int(sisi)
#print(Luas)

#Challenge
sisiAtas = input("masukan sisiAtas :")
sisiBawah = input("masukan sisiBawah :")
tinggi = input("masukan tinggi :")

Luas = int(int(tinggi)*int(sisiAtas + sisiBawah)/2)
print(int(Luas))
