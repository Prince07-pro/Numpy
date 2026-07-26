#indexing and slicing

import numpy as np

a1 = np.arange(10)#n-1 last ele..
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)

#index

print(a1[-1]) #1-d array index as normal as python
#start at 0 and nagetive

print(a2[1,2])
#2-d array index [row,column]
#row and column start at 0

print(a3[0,1,1])
#3-d array index[2-d array index, row,column]

##slicing

print(a1[2:9:2])
#same as python 1D

print(a2[0,:])
# 2D-0=row and column[row,column]

print(a2[1:,1:3])
print(a2[::2,::3])
print(a2[0::2,1::2])#2D array

print(a3[1])#3D
print(a3[1,:,1])
print(a3[2,1:,1:])
print(a3[0::2,0::3,0::2])
#[2D array index,row,column]