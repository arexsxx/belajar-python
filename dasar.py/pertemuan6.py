#1.fitur input data
#2.Tampilan data (semua)
#3.Tampilkan data berdasarkan NIM
#4.Tampilkan data berdasarkan NAMA
#5.Cari data berdasarkan NIM
#6.Cari data berdasarkan NIM (yg ditampilkan data dan nilainya)
#7.Cari nilai 

#Note:
#1. mengatasi data tampil jika datanya kosong
#2. Tampilkan data semunya menggunakan perulangan
#3. Cari nilai gunakanlah 


#SOP kuis:
#1. soal dibagikan nanti malam(dini hari)
#2. waktu 60 menit
#3. penilaian berdasarkan fitur
#4. Diberi else disemua kondisi

data=[]
def inputData():
    inputNama=input("masukkan nama: ")
    inputNim=int(input("masukkan NIM anda: "))
    nilaiA=int(input("masukkan nilai Alpro: "))
    nilaiB=int(input("masukkan nilai Matematika: "))
    nilaiC=int(input("masukkan nilai Agama: "))
    dataBaru=[]
    dataBaru.append(inputNama)
    dataBaru.append(inputNim)
    dataBaru.append(nilaiA)
    dataBaru.append(nilaiB)
    dataBaru.append(nilaiC)
    data.append(dataBaru)
def tampilanData():
    for i in data:
        print("="*10)
        print(i)
        print("="*10)
def tampilDataNim():
    for i in data:
        print(i[1:])        
while True:
    print("Pilihan menu")
    print("="*10)
    print("1.masukkan data")
    print("2.liat data")
    print("3.liat data berdasarkan NIM") 
    inputMenu=int(input("pilihlah salah satu dari pilihan tersebut: ")) 
    if inputMenu==1:
        while True:
            inputData()
            ulang=input("apakah anda ingin memasukkan data lagi?, y/t: ")
            if ulang=="t":
                break
            elif ulang=="y":
                continue
            else:
                print("pilihan salah")
    elif inputMenu==2:
        tampilanData()
    elif inputMenu==3:
        while True:
            liat=input("apakah anda ingin melihat data berdasarkan NIM? y/t: ")
            if liat=="t":
                break
            elif liat=="y":
                tampilDataNim()
            else:
                print("pilihan tidak ditemukan")
    else:
        print("pilihan anda salah")
        break    







