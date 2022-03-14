import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import joblib

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass', 'pedi', 'age' , 'class']

df = pd.read_csv(url, names=names)
print(df.head())

array = df.values
X = array[:,:8]
y = array[:,8]

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state = 101)

#Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

#Accuracy of Model
result = model.score(X_test, y_test)
print(f'The accuracy score is :{result}')

#Model Saving
filename = 'diabetic_80.pkl'
joblib.dump(model, filename)

#Prediction


