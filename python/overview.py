marks= 70
# int(input("Please Enter the Student Marks : "))
match marks:
    case m if m >= 90:
        print("A")
    case m if m >= 80:
        print("B")
    case m if m >= 70:
        print("C")
    case _:
        print("Fail")

        # remeber that we can create the fucntion with 4 types are there 
        # 1. No parameter and No return type
#         2. No parameter and return type
# 3. parameter and  no return type
# 4.  parameter and return type

score ={
    90:"A Grade",
    80:"B Grade",
    85:"C Grade",
    75:"D Grade"
}

print (score)
print(score.get(82))
print(score.get(65,"Fail"))
