import numpy as np
# random.randint has start, stop+1, number of integers
array1 = np.random.randint(0,2,6)
print("Array one:")
print(array1)
array2 = np.random.randint(0,2,6)
print("Array 2:")
print(array2)
print("Check if these two arrays are equal : ")
is_equal = np.allclose(array1, array2)
print(is_equal)