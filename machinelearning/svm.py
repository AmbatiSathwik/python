import sklearn
import numpy as np
import pandas as pd
from sklearn import svm, datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

data = datasets.load_breast_cancer()
#print(data.feature_names)
#print(data.target_names)

X = data.data
Y = data.target

names = ['malignant' 'benign']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1)

model = svm.SVC(kernel = 'linear')
model.fit(x_train, y_train)

acc = model.score(x_test, y_test)
print(acc)

kneigh = KNeighborsClassifier(n_neighbors = 5)
kneigh.fit(x_train,y_train)

acc2 = kneigh.score(x_test, y_test)
print(acc2)
