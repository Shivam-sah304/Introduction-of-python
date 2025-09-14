# Write a Python function that rotates a square matrix (n×n) by 90° clockwise.
list =[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
import numpy as np
np_list=np.array(list)
print(np_list.shape)

print(np_list.transpose())

