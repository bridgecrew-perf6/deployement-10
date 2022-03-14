import pickle

#Load model
model = pickle.load(open('diabetic_80.pkl', 'rb'))
output = model.predict([[1,2,3,4,5,6,7,8]])
if output[0]==1:
    print('The person is diabetic')
else:
    print('The person is NOT diabetic')

