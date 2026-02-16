import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
X = np.array([[1,2],[1,4],[1,0],[10,2],[10,4],[10,6]])
#I guess cluster is nothing but the similar data is grouping them self
#here we have cluster 1 as start with [1]
# and the second one is start with [10]

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

plt.scatter(X[:,0],X[:,1],c = kmeans.labels_)

plt.show()