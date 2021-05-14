import sklearn
from sklearn import datasets
from sklearn.preprocessing import scale
from sklearn.cluster import KMeans

data = datasets.load_digits()

#print(scale(data.data))

#print(data.target)

model = KMeans(n_clusters=10,n_init=10)

model.fit(data.data)
print(model.labels_)
print(model.cluster_centers_)

