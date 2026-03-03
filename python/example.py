#pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# data ={
#     "Age" : [22,24,28,30,36,45],
#     "Salary" : [25000,32000,38000,42000,45000,56000],
#     "Department" : ["IT","HR","IT","Finance","HR","Finance"]
# }

df = pd.read_excel("student2.xlsx",engine="openpyxl")

print(df)
# sns.lineplot(x=df["Age"],y=df["Marks"], data=df)
# plt.title("LinePlot for the age Marks")
# plt.show()


sns.set_style("whitegrid")
# sns.scatterplot(
#     x=df["Age"],
#     y=df["Marks"],
#     data=df
#     )
# plt.title("Correlation Heatmap")
# plt.show()



# print(df)

# sns.barplot(x="Department",y="Salary",data=df)
# plt.title("Average Salary")
# plt.title("Age vs Salary")
# plt.show()


# sns.countplot(x="Department",data=df)
# plt.title("Employe count per department")
# plt.show()

# sns.histplot(df["Salary"],bins=5,kde=True)
# plt.title("Salary Distrubution")
# plt.show()


sns.boxplot(x=df["Age"],y=df["Marks"], data=df)
plt.title("Salary By Department")
plt.show()

# sns.violinplot(x="Department",y="Salary",data=df)
# plt.title("Salary Distrubution shape")
# plt.show()

# corr=df[["Age","Salary"]].corr()
# sns.heatmap(corr, annot=True,cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()
