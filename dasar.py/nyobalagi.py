# (IF DAN ELSE)
# def NilaiUjian (angka):
#     if angka >= 80:
#         huruf ="A"
#     else:
#         if angka >=60:
#             huruf ="B"
#         else:
#             if angka >=40:
#                 huruf ="C"
#             else:
#                 huruf = "D"
#     print ("hasil nilai ujian dalam sub prpogram = " + huruf)
#     return huruf

# # Main
# print("Masukkan nilai ")
# angka = float(input())
# tempatHuruf = NilaiUjian(angka)
# print("Hasil Nilai ujian angka ke huruf (dalam main) = " + tempatHuruf)



# def tesInput():
#     name=input("what is your name ? ")
#     print("nice to meet you " + name + "!")
#     age=str(input("your age "))
#     print("so, you are already "+ age + " years old, " + name + "!")

# tesInput()

##PERULANGAN
# pilih=int(input("seberapa sayangkah kamu?\n1.sayang banget\n2.sayang ga banget\n3.sayang tok\n\npilih satu aja ya : "))

# def sayangBanget():
#     print(f"I love you so much")

# def sayangGaBanget():
#     print(f"I love you")

# def sayangTok():
#     print(f"muuah")

# if pilih==1:
#     sayangBanget()
# elif pilih==2:
#     sayangGaBanget()
# elif pilih==3:
#     sayangTok()                   







# from turtle import*
# color("red")
# begin_fill()
# pensize(5)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill()
# exitonclick()






# data = []
# def inputList():
#     global data
#     inputKode=input("masukkan kode: ")
#     inputBarang=input("masukkan barang: ")
#     dataBaru=[]
#     dataBaru.append(inputKode)
#     dataBaru.append(inputBarang)
#     data.append(dataBaru)
# def cariList():
#     cariBarang =input("Masukkan kode untuk mencari barang: ")   
#     for i in data:
#         if i[0] == cariBarang:
#             print(i) 
#             break
#     else:
#         print("kode yang ada masukkan salah")
# def liatList():
#     global data
#     for i in data:
#         print(i)

# while True:
#     print("pilihan menu: \n\n1.Input kode: \n2.Liat barang: \n3.Cari list: \n4.exit")
#     inputMenu=input("pilih salah satu : ")
#     if inputMenu=="1":
#         while True:
#             inputList()
#             ulang = input("apakah ingin input lagi? y/t: ")
#             if ulang == "t":
#                 break
#             elif ulang =="y":
#                 continue
#             else:
#                 print("input yang anda masukkan salah")
#     elif inputMenu=="2":
#         cariList()
#     elif inputMenu=="3":
#         liatList()
#     elif inputMenu=="4":
#         break
#     else:
#         print("angka yang anda masukkan salah")



        


































