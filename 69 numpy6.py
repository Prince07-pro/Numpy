# array function

import numpy as np

a = np.random.random((3,3))
a = np.round(a*100)
a1 = np.arange(12).reshape(3,4)
print(a)

#max/min/sum/product
b = np.max(a)# all array
print(b)

b1 = np.max(a,axis=0)# any row or column
print(b1)# 0->column 1->row

c = np.min(a)
print(c)

c1 = np.min(a,axis=1)
print(c1)

d = np.sum(a)
print(d)

e = np.prod(a)
print(e) 

#mean/median/std/var

f =np.mean(a)
print(f)

f1 =np.mean(a,axis=0)
print(f1)

g =np.median(a)
print(g)

g1 =np.median(a,axis=1)
print(g1)

h =np.std(a)#standard deviation
print(h)

h1 =np.std(a,axis=1)
print(h1)

i =np.var(a)#variant
print(i)

i1 =np.var(a,axis=0)
print(i1)

#trigometric fun

j = np.sin(a)
print(j)

#log and exponents

k  = np.log(a)
print(k)

l = np.exp(a)
print(l)


#round/floor/ceil

m = np.round(np.random.random((2,3))*100)
print(m)#round is 24.675(nearest integer show) than round show a 25.

n =np.floor(np.random.random((2,3))*100)
print(n)#floor is 24.999 than floor show a 24

o = np.ceil(np.random.random((2,3))*100)
print(o)#24.456 than ceil show a 25

#transporse
p = np.transpose(a1)
print(a1)# convert row to column

#ravel(any dime.. array convert to 1D array)
q = np.ravel(a1)
print(q)

