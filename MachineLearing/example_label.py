import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
#feeding excel file to the data

data = pd.read_excel("student_practice.xlsx", engine="openpyxl")
print(data)


df =pd.DataFrame(data)
le =LabelEncoder()

# Education_Level,City, Status

# df["Education_Level"] = le.fit_transform(df["Education_Level"])
# df["City"] = le.fit_transform(df["City"])
df["Status_Encoded"] = le.fit_transform(df["Status"])
print(df)

X= df[["Marks"]]
Y= df["Status_Encoded"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)
#obejction creating
#model= RandomForestClassifier()
model = LogisticRegression()
model.fit(X_train,Y_train)

Y_predict = model.predict(X_test)

print("Accuracy :",accuracy_score(Y_test,Y_predict) )

print("Confusion Matrix : ",confusion_matrix(Y_test,Y_predict))

print("Classfication Report :",classification_report(Y_test,Y_predict))

sns.heatmap(confusion_matrix(Y_test,Y_predict),annot=True)
plt.show()