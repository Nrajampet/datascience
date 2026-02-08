#check out this website prepinsta -- interview questions

import numpy as np

#converting the values--by using np.where fucntion

marks = np.array([90,50,80,40,50,60,75])

result = np.where(marks>50, "pass","fail")
print(result)

# arr1= np.array([[1,2,3],[5,6,7]])
# print(arr1.sum(axis=0)) #by using the axis=0 we can get the column addition
# print(arr1.sum(axis=1)) #by using the axis=0 we can get the row addition

# arr1= np.array([90,50,80,40,50,60,75])
# print(arr1.argmax())# -- it will dispay the position of the maximum value in that array
# print(arr1.argmin())# --it will dispay the position of the minimum value in that array


# marks = np.array([90,50,80,40,50,60,75])
# passed = marks[marks>50]
# print(passed)

# # marks[marks<50] =0
# # print (marks)
# marks2 = marks[1:4]
# print(marks2)

# #Shape and flat 
# arr=np.array([[1,2,6],[3,4,5]])
# print(arr.shape)
# flat=arr.flatten()
# print(flat)
