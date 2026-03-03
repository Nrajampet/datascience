import pandas as pd
import openpyxl 

#  pip install xlrd -mac use engine xlrd
res = pd.read_excel("student2.xlsx", engine="openpyxl")
print(res)




# res = pd.read_csv('student.csv')
# print(res)
# print(res["RollNo"])
# print(res[["RollNo","Marks"]])
# print(res.loc[0]) #loaction using position old apporch 
# print("______________________")
# print(res.iloc[0])


# print(res[res["Marks"]>70])
# print(res[(res["Marks"]>70) & (res["Age"]>21)])

# res["Passed"] = res["Marks"]>=70#add new column
# print(res)
# print("______________________________")
# print(len(res))
# print("______________________________")
# res.drop("Passed", axis=1, inplace=True) # axis=1 column inpalce is 
# print(res)
# res.drop(6,inplace=True) # for the axis=0 defaults and also 
# # # inplace is need to be ture if you want that action need to be done
# print(res)
# dl = res.droplevel(2) # need to get the clarity on this 
# print(dl)
# res.drop(["Passed","Name"], axis=1, inplace=True)
# print(res)
# print(len(res))
# print("______________________________")
# res.drop([2,5],inplace=True)
# print(res)
# print(len(res))
# data ={
#     "Name":["Emp1","Emp2","Emp3","Emp4","Emp5","Emp6","Emp7"],
#     "Age":[21,22,25,28,27,26,32],
#     "Salary":["75k","80k","92k","89k","80k","80k","1.5lakhs"]
# }

# res= pd.DataFrame(data)
# print(res)
#to get the 5row use the head fun same
#  for the last 5 rows use this tail 
# to the shape use the shap fuction 
# to column use the columns function 
# to diplay the data types use the info

 
# print(res.shape)
#print(res.head(1))
# print(res.tail)
# print(res.columns)
# print(res.info())


# to define series of data
# series = pd.Series([10,20,30,40,50,60,70]) #--S is captial one
# print(series)
#to instilizie the git repo use init
# to config 
# git config --golbal user.name
# git config --global user.email "username@email.com"
# to add file 
# git add.
# to commit
# git commit -match
# to connect remotely
# gir remote add origin uURL
# git push -u origin master