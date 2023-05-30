import datetime
x = datetime.datetime.now()
data =[]
def inputList():
    global data
    inputNIM = input("Masukkan data NIM : ")
    inputNama = input("Masukkan data nama : ")
    dataBaru =[]
    dataBaru.append(inputNIM)
    dataBaru.append(inputNama)
    dataBaru.append(x)
    data.append(dataBaru)
def cariList():
    cariData = input("Masukkan NIM untuk mencari data : ")
    for i in data:
        if i[0] == cariData:
            print(i)
            break
    else :
        print("Data yang Anda cari tidak ditemukan")

def liatList():
    global data
    for i in data:
        print("="*10)
        print(i)
        print("="*10)
while True:
    print("="*10)
    print("Pilihan menu")
    print("="*10)
    print("1. Input data")
    print("2. Liat data")
    print("3. Cari data")
    print("4. Exit")
    print("="*10)
    inputMenu = input("Masukkan pilihan menu [1-4] : ")
    if inputMenu == "1":
        while True:
            inputList()
            ulang = input("Apakah ingin input lagi ? y/t : ")
            if ulang == "t":
                break
            elif ulang == "y":
                continue
            else:
                print("Pilihan yang Anda masukkan salah!")
    elif inputMenu =="2":
        liatList()
    elif inputMenu =="3":
        cariList()
    elif inputMenu == "4":
        break
    else :
        print("Angka yang Anda masukkan salah")


