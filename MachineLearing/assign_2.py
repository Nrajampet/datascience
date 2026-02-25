import numpy as np
arr= np.array([12,55,-5,102,44,88,-20,150])
print(arr[arr > 50]) # >50

arr[arr < 0]=0
print(arr)

count =np.sum(arr % 2 == 0)
print(count)

indices = np.where(arr > 100)
print(indices)

arr6=np.arange(12)
arr7=np.arange(24)
arr_3X3 =arr6[:9].reshape(3,3)
print(arr_3X3)
rand_arr = np.random.randint(10, 101, size=(3, 3))
print(rand_arr)

arr_3X3_1 = arr7[:9].reshape(3, 3)
print(arr_3X3_1)
res = arr_3X3 @ arr_3X3_1
print(res)

transpose = arr_3X3 . T
print(transpose)

det = np.linalg.det(arr_3X3)
print(det)



A = np.array([[1, 2],[3, 4]])
b =np.array([5, 11])

X = np.linalg.solve(A,b)
print(X)

inv = np.linalg.inv(A)
print(inv)
