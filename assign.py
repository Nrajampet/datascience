#here we are using the excel file to create a graph

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel("student2.xlsx",engine="openpyxl")
names=df["Name"]
marks=df["Marks"]
colors=[]
for m in marks:
    if m>=85:
        colors.append('Green')
    elif m>=75:
        colors.append('Blue')
    elif m>=70:
        colors.append('orange')
    else:
        colors.append('red')
bars= plt.bar(names,marks,color=colors)
for bar in bars:
    plt.text(
        bar.get_x()+bar.get_width()/2,# to render the text all we need to use the the gap between the starting line 
            # to the bar and half of the width it willl be like this= gap+width/2 
        bar.get_height(),
        bar.get_height(),
        ha="center",#predefined ha,va
        va="bottom"
    )

plt.title("Student Marks")
plt.ylabel("Marks")
plt.show()
# print(df)
# sns.lineplot(x="Age",y="Salary", data=df)

