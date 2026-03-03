import numpy as np
from sklearn.decomposition import PCA

X= np.array([[2,4,6],
             [3,6,9],
             [4,8,9],
             [5,10,12]])

model = PCA(n_components=2)
X_new= model.fit_transform(X)

print(X_new)