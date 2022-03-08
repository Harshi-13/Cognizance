import numpy as np
no = []
print("Enter starting number")
start_number = int(input())
print("Enter ending number")
end_number = int(input())
for x in range(start_number, end_number+1):
    no.append(x)

print("Given array:")
print(no)
z = 5
l = len(no)
new_number = np.zeros(l + (l-1)*(z))
new_number[::z+1] = no
print("Output:")
print(new_number)
