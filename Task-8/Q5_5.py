import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)
print ("print 4 rows and 3 columns")
print(newarr)

newarr = arr.reshape(2, 3, 2)
print ("print 3 rows * 2 columns with 2 matrix ")
print(newarr)

print("print 3 * 4 ")
newarr = arr.reshape(3,-1)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("single array")
print(arr.reshape(2, 4).base)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print('print 2 * 2 * 2 matrix ')
print(newarr)