import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report


data ={
    "tenure" : [1,3,5,10,14,5,6,2],
    "monthly_charges":[50,60,80,45,70,90,55,85],
    "contract-types":["Month-to-Month","One Year","Two Year","Month-to-Month","One Year","Two Year","Month-to-Month","One Year"],
    "churn":["Yes","NO","Yes","NO","Yes","NO","Yes","NO"]
}

df =pd.DataFrame(data)
le =LabelEncoder()
df["contract-types"] = le.fit_transform(df["contract-types"])
df["churn"] = le.fit_transform(df["churn"])

X= df.drop("churn",axis=1)
Y= df["churn"]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)
#obejction creating
model= LogisticRegression()
model.fit(X_train,Y_train)

Y_predict = model.predict(X_test)

# print("Accuracy :",accuracy_score(Y_test,Y_predict) )

# print("Confusion Matrix : ",confusion_matrix(Y_test,Y_predict))

# print("Classfication Report :",classification_report(Y_test,Y_predict))

# sns.heatmap(confusion_matrix(Y_test,Y_predict),annot=True)
# plt.show()

new_customer =np.array([[4,65,0]])
prediction= model.predict(new_customer)
if prediction[0]==1:
    print("Churn")
else:
    print("NO")