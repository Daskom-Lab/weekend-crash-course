import matplotlib.pyplot as plot
import pandas as pd
import numpy as np

df=pd.read_csv('titanic.csv')
plot.scatter(df['Fare'],df['Age'],c=df['Survived'])
plot.xlabel('Fare');plot.ylabel('Age')
#kita plot dulu semua yang selamat apa engga, kelompok umur, dan apa mereka selamat apa engga
#plot.show()

# The task of a linear model is to find the line that best separates the two classes, 
# so that the yellow points are on one side and the purple points are on the other.
# dengan logistic regression kita mencari sebuah garis yang bisa membagi antara ungu dan kuning, hasilnya:
x=np.array(range(500))
y=x-30
plot.plot(x,y,label='y=x-30')
plot.show()