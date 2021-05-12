import numpy as np
import pandas as pd
from sklearn import preprocessing,neighbors,linear_model
from sklearn.model_selection import train_test_split

data = pd.read_csv('car.data')
#print(data.head())
encode = preprocessing.LabelEncoder()
buying = encode.fit_transform(list(data['buying']))
maintain = encode.fit_transform(list(data['maintain']))
doors = encode.fit_transform(list(data['doors']))
persons = encode.fit_transform(list(data['persons']))
lug_boot = encode.fit_transform(list(data['lug_boot']))
safety = encode.fit_transform(list(data['safety']))
cls = encode.fit_transform(list(data['class']))

X = list(zip(buying,maintain,doors,persons,lug_boot,safety))
Y = list(cls)

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size = 0.1)

kneigh = neighbors.KNeighborsClassifier(n_neighbors=9)
kneigh.fit(x_train,y_train)

acc = kneigh.score(x_test,y_test)
print(acc)

predict = kneigh.predict(x_test)

name = ['unacc','acc','good','vgood']
for i in range(len(predict)):
    print(name[predict[i]],'       ',name[y_test[i]])
