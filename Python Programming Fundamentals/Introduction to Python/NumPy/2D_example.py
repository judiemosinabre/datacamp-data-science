import numpy as np

students = [[10, 5, 2, 4, 5],
            [3, 8, 9, 2, 1],
            [4, 7, 1, 6, 3]]

#3D array
np_students = np.array(students)

# print(type(np_students))

#all 2nd column
print(np_students[:,1]) 

#all 3rd row
print(np_students[2][:])
print(np_students[2,:])
