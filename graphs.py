import matplotlib.pyplot as plt
# task=["Task1","Task2","Task3","Task4"]
# status=[90,85,70,60]
# plt.barh(task,status,color="coral")
# plt.xlabel("Completion")
# plt.ylabel("Task")
# plt.title("Progress Tracker")
# plt.show()

#scatter plot
x=[1,2,3,4,5]
y=[10,20,25,30,45]
sizes=[100,200,300,400,450]
colors=[10,20,30,40,50] # to give the control to the matplot lib can decide the colors
plt.scatter(x,y,s=sizes,c=colors,cmap="viridis")#ot's show the gradiance viridis
#t display color meter
plt.colorbar(label="Color Scale")
plt.xlabel("X-Values")
plt.ylabel("Y-Values")
plt.title("Adavanced Scatter Plot")
plt.show()

# import matplotlib.pyplot as plt
# to create the bars by using pyplot
# students=["ALice","Ben","Clarie","Derik"]
# marks=[72,85,89,95]
# bars = plt.bar(students,marks,color="Blue")
# for bar in bars:
#     plt.text(
#         bar.get_x()+bar.get_width()/2,# to render the text all we need to use the the gap between the starting line 
#             # to the bar and half of the width it willl be like this= gap+width/2 
#         bar.get_height(),
#         bar.get_height(),
#         ha="center",#predefined ha,va
#         va="bottom"
#     )

# plt.title("Student Marks")
# plt.ylabel("Marks")
# plt.show()



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

# days=[1,2,3,4,5]
# sales=[200,400,600,800,1000]
# profit=[50,150,300,450,600]

# plt.plot(days, sales, label="Sales",marker="o")
# plt.plot(days, profit, label="Profit",marker="s")

# plt.grid(True)
# plt.title("Sales Vs Profits")
# plt.xlabel("Days")
# plt.ylabel("Amount")
# plt.legend()
# plt.show()


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
