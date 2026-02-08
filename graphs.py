import matplotlib.pyplot as plt
# lan=["Java","Python","C","Embeded C","Rust"]
# usage=[40,20,10,15,15]
# plt.pie(usage, 
#         labels=lan,
#         autopct="%1.1f%%",
#         colors=["gold","blue","pink","Yellow","Green"],
#         explode=[1,0,0,0,0],
#         shadow=True,
#         startangle=120)
# plt.title("Language Market share")
# plt.show()



# x=[1,2,3,4,5]
# y=[5,10,15,20,25]
# plt.plot(x,y, color="red",linestyle="--",linewidth=2,marker="o",markersize=10)
# plt.grid(True)
# plt.title("Custome line graph")
# plt.xlabel("X-Values")
# plt.ylabel("Y-Values")
# plt.show()

days=[1,2,3,4,5]
sales=[200,400,600,800,1000]
profit=[50,150,300,450,600]

plt.plot(days, sales, label="Sales",marker="o")
plt.plot(days, profit, label="Profit",marker="s")

plt.grid(True)
plt.title("Sales Vs Profits")
plt.xlabel("Days")
plt.ylabel("Amount")
plt.legend()
plt.show()


# plt.scatter(x,y)
# plt.xlabel("X-Values")
# plt.ylabel("Y-Values")
# plt.title("Scatter Plot")
# plt.show()


# students=["Alice","Ben","Clarie","Dean","Eric"]
# marks=[74,75,68,85,95]
# plt.bar(students,marks)
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("1st Semester Marks")
# plt.show()





# import matplotlib 
# print(matplotlib.__version__) 
# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[10,20,30,40,50]
# plt.plot(x,y)
# plt.xlabel("X-values")
# plt.ylabel("Y-values")
# plt.title("Sample Line Graph")
# plt.show()

# lan=["Java","Python","C","Embeded C","Rust"]
# usage=[40,20,10,15,15]
# plt.pie(usage, labels=lan,autopct="%1.1f%%",colors=["gold","blue","pink","Yellow","Green"],explode=[1,0,0,0,0])
# plt.title("Language Market share")
# plt.show()
