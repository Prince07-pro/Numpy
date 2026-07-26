#dot product(if only (3,4),(4,3) 1st of column = 2nd row)
import numpy as np

a = np.arange(12).reshape(3,4)
b = np.arange(12,24).reshape(4,3)

f = np.dot(a,b)
print(f)