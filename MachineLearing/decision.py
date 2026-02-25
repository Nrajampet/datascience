import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

X= np.array([[25,40000],
             [32,50000],
             [36,56000],
             [40,65000],
             [45,70000]])

y = np.array([0,1,1,0,1])

model =DecisionTreeClassifier(criterion='gini')

model.fit(X,y)
predict = model.predict([[43,61000]])

print(predict)
# plt.plot(X,y, color="red",linestyle="--",linewidth=2,marker="o",markersize=10)
# plt.title("Decision Tree")
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.show()

plt.figure(figsize =(10,6))
tree.plot_tree(model,filled=True)
plt.show()