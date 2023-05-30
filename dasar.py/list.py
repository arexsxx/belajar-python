##Penulisan list

##Indexing
#        0/-4     1/-3     2/-2    3/-1
# data = ["paijo","slamet","supri","parman"]
# print("ini adalah data awal",data)

# #Manipulasi list

# #Insert (Menambahkan nilai berdasarkan index)
# data.insert(1,"yanto") #Index,nilainya
# # print(data)
# # data.insert(2,"surya")
# # print(data)

# ##Append (Menambahkan nilai pada akhir list) biasanya digunakakn pada database##
# data.append("rizal")
# data.append("dandi")
# data.append("mail")
# #print(data)

# #Extend (Menambahkan list didalam list)
# data_baru = [10,20,30,40,]
# data.extend(data_baru)
# print(data)


# ##Mengedit data##
# data[1] = "Mr.bean"
# print(data)

# ##Mengahapus data##
# #remove
# data.remove(10)
# data.remove("rizal")
# #print(data)


# dataAngka = [20,40,30,10,60,50]
# #Fungsi sort (mengurutkan dari yang terkecil)
# dataAngka.sort(reverse=True)
# # print(dataAngka)
# #Fungsi reverse (membalikkan urutan)
# # dataAngka.reverse()
# print(dataAngka)



#List lanjutan
#Slicing / pemotongan
# data = ["paijo","slamet","supri","parman"]
# print(data[2])# Mengambil data list berdasarkan index
# print(data[1:3]) #Index awal: index setelahnya
# slicing_data = data[1:2]
# slicing_data_awal_sampai_akhir = data[2:]#data awal sampai akhir
# slicing_batas_data_akhir = data[:3] #Kasih batas datanya




#List 2D
data = [
    ["5220411102","Ervin khoirus","Agustus"],
    ["5220411101","paijo subejo","november"]
]
# print(data)
print(data[1][1])

# z = 0
# while z < len(data):
#     print(data[z][1])
#     z = z+1




