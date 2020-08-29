import pandas as pd
from sklearn.linear_model import LogisticRegression
df=pd.read_csv('titanic.csv')
df['male']= df['Sex']=='male'
x= df[['Fare','Age']].values
y= df['Survived'].values
print(x)
print(y)
model = LogisticRegression()
model.fit(x,y)
print(model.coef_,model.intercept_);
#[[ 0.01615949 -0.01549065]] [-0.51037152] artinya garis pemisah => 0=0.01615949x + -0.01549065y + -0.51037152
X=df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
model.fit(X,y)
print (model.predict(X[:5]))
print (y[:5])
#accuracy score:
y_pred=model.predict(X) #y_pred isi dari semua prediksi dari target which is y
totalTrue = (y==y_pred).sum()
print (totalTrue)
totalPassenger = y.shape[0]
print (totalPassenger)
print ("Akurasi prediksi: ");print(totalTrue/totalPassenger)