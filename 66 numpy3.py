#numpy attributes

import numpy as np

a1 = np.arange(10)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

#ndim = find a dimension of array
p=a1.ndim
print(p)

# shape = every dimension to give a column or row

r = a2.shape
print(r)

#size = number of item

q = a3.size
print(q)

#itemsize = give a size of array

s = a3.itemsize
print(s)

#dtype = array datatype

print(a3.dtype)