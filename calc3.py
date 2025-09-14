# Largest Element in Each Row of a 2D List
list=[[3, 5, 1],
 [12, 7, 9],
 [4, 2, 8]]
import numpy as np
np_list=np.array(list)
#find the maximum of each row
print(np.maximum(np_list[:,0],np_list[:,1],np_list[:,2]))
#find the minimum value as well
print(np.minimum(np_list[:,0],np_list[:,1],np_list[:,2]))
