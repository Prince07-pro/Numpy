# create a array using this function
import numpy as np
p = np.arange(1,11)
print(p)#arange use to a create any range of array 

#reshape fun
r = np.arange(1,11).reshape(2,5)
print(r)#reshape (row, column)

#ones or zeros fun(initilize to array)

t=np.ones((3,4))
print(t)#ones all 1.

s=np.zeros((3,4))
print(s)#zeros all 0. 

#random fun(initilize to array)
w = np.random.random((3,4))
print(w)#initilize all random element.

#linear space fun

u = np.linspace(-10,10,10)
print(u)#given range to generate equal point element

#identity (create a identity matrix)
o=np.identity(3)
print(o)