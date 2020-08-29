import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('titanic.csv')
plt.scatter(df['Age'],df['Fare'])
#format si scatter itu akan di plot scatter (x,y)
plt.xlabel('Age');plt.ylabel('Fare')
#Kasih nama biar ga bingung
plt.scatter(df['Age'],df['Fare'],c=df['Pclass'])
#c itu ngasih warna (colour)
#s itu ngasih ukuran (size)
plt.plot([0, 80], [85, 5])
#ngasih garis dari x1 y1 ke x2 y2
plt.show()
#tampilkan