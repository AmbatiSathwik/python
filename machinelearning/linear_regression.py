import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

check = 0
data = pd.read_csv('data.csv')
data = data[['G1','G2','G3','studytime','failures']]
    
X = np.array(data.drop(['G3'], 1) )
Y = np.array(data['G3'])
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1)    
   
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1)
linear = LinearRegression()
linear.fit(x_train, y_train)
accuracy = linear.score(x_test,y_test)

predict = linear.predict(x_test)
for i in range(len(predict)):
    print(x_test[i],'         ', predict[i], '        ' ,y_test[i])
