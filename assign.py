#here we are using the excel file to create a graph

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel("student2.xlsx",engine="openpyxl")
names=df["Name"]
marks=df["Marks"]
bars= plt.bar(names,marks,color="blue")
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