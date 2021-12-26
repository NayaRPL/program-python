matrix1 = [[1 , 4 , 3 , 2] ,
           [2 , 3 , 5 , 6] ,
           [3 , 8 , 9 , 4] ,
           [1 , 5 , 9 , 2]]

matrix2=  [[1 , 4 , 3 , 3] ,
           [4 , 3 , 5 , 6] ,
           [9 , 8 , 5 , 4] ,
           [1 , 2 , 9 , 2]]
print("cara menjumlahkan matrix")
hasil=[]
for i in range(len(matrix1)):
    baris=[]
    for j in range(len(matrix1[i])):
        baris.append(matrix1[i][j]+ matrix2[i][j])
    hasil.append(baris)
for baris in hasil:
    print(baris)

print("cara mengalihkan matriks")
hasil =[]
for i in range (len(matrix1)):
    baris=[]
    for k in range(len(matrix2[0])):
        val = 0
        for j in range(len(matrix1[i])):
            val +=matrix1[i][j] * matrix2[j][k]
        baris.append(val)
    hasil.append(baris)
print("hasil perkalian 2 matrix :")
for baris in hasil:
    print(baris)


list=[7,1,14,21,28,42,35]
x=(int(input("masukkan nilai yang ingin di cari:")))
idx = -1#daftar indeks yang mau di cari
            
for i in range(len(list)):
    if list [i] == x:
        idx=i
        break

if idx == -1:
    print("angka",x,"tidak ditemukan")

else:
    print("angka",x,"ditemukan dalam pada indeks",idx)


                           
        
