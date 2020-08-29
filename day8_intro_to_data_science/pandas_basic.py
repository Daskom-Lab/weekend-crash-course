import pandas as pd
df=pd.read_csv('titanic.csv') #df itu dataframe (tabel berisi judul di index dan kolom)
print(df.head()) #ngebaca 5 row pertama
print(df.describe()) #nulis statistiknya
#select cuman fare:
col = df['Fare']
print(col)
# select beberapa aja
small_df=df[['Age','Sex','Survived']] #DOUBLE SQUARED BRACKETS
print(small_df.head())
#buat series baru dari data yang awal, terus nilainya true kalau male
df['isMale']=df['Sex']=='male'
print(df.head())