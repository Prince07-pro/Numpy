# stacking and spiliting

import numpy as np

a = np.arange(12).reshape(3,4)
b = np.arange(12,24).reshape(3,4)

# 1 horizontal stacking
#ex =2*2 + 2*2 = 2*4

c = np.hstack((a,b,a))
print(c)

#2 vertical stacking

d = np.vstack((a,b))
print(d)

# spiliting

# 1 horizontal spiliting

e = np.hsplit(a,2)
print(e)

# 2 vertical spiliting

f = np.vsplit(b,3)
print(f)