import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier 

X = np.array([[1,60],
              [2,65],
              [3,70],
              [4,80],
              [5,85],
              [6,90],
              [7,95],
              [8,100]])

y= np.array([0,0,0,0,1,1,1,1])

model = RandomForestClassifier(n_estimators =10, random_state = 42)
model.fit(X,y)

prediction = model.predict([[4,70]])

acc= model.score(X,y)
print(prediction)
print (acc)