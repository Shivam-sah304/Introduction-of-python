# Sum of All Elements in a 2D List and find mean and median of 2nd column
list=[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
import numpy as np
np_list=np.array(list)
print(type(np_list))
print(np_list)
print(np_list.sum())
#finding mean of second column
print(np.mean(np_list[:,1]))
#finding the median of third column
print(np.median(np_list[:,2]))