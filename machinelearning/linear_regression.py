import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
data = data[['G1','G2','G3','studytime','failures','sex']]
    
X = np.array(data.drop(['G3'], 1) )
Y = np.array(data['G3'])
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1)    
  
#training    
#for _ in range(10):
#    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1)
#    linear = LinearRegression()
#    linear.fit(x_train, y_train)
#    
#    accuracy = linear.score(x_test,y_test)
#    print(accuracy)
#    if check < accuracy:
#        check = accuracy
#        with open('grade.pickle', 'wb') as fh:
#            pickle.dump(linear, fh)

            
load = open('grade.pickle', 'rb')
linear = pickle.load(load)
predict = linear.predict(X)
acc = linear.score(x_test,y_test)
print(acc)

p = 'G1'

plt.scatter(data[p],predict)
plt.xlabel(p)
plt.ylabel('prediction')

plt.scatter(data[p],data['G3'])
plt.xlabel(p)
plt.ylabel('Real One')
