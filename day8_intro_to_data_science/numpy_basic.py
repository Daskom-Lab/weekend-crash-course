import pandas as pd

#konversi pandas dataset menjadi numpy array, pertama kita konversi fare dulu
#0, deklarasi data apa yang mau kita pake
#1, ambil fare di pandas, terus coba print VALUES nya

df=pd.read_csv('titanic.csv') #0)
print(df['Fare'].values) #1) ini hasilnya bakal array 1 dimensi yang elemennya nilai2 Fare
#pandas berdiri diatas numpy, jadi santai aja sampe sini belum perlu import numpy
print('\n')
#atau, bisa konversi ke array 2 dimensi pakai .values juga
arr=df[['Pclass','Fare','Age']].values
print(arr)
print('\n')
#numpy punya .shape, untuk melihat ukuran 2d array yang dia handle
print("array kita ada x baris dan y kolom (x,y):")
print(arr.shape)
#well si arr udah berupa numpy array 
print('\n')
print('spesifik,baris pertama (0, orang pertama) kolom kedua (1, Fare) :');print(arr[0,1])
print('seluruh isi dalam baris 0 (orang pertama): ');print(arr[0])
print('seluruh isi dalam kolom 2 (Age): ')
print(arr[:,2]);print('\n')
print('\nMasking: ')
mask=arr[:,2]<18 #ambil yang agenya dibawah 18 aja
print(arr[mask])#pasang filter buat tampilin data yang dibawah 18 aja
#atau arr[arr[:,2]<18] juga bisa sama aja
print('total anak-anak yang selamat:')
print(mask.sum())
#atau print((arr[arr[:,2]<18),sum()) juga bisa

