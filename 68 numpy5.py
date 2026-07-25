# array operation
import numpy as np
a = np.arange(12).reshape(3,4)
b = np.arange(12,24).reshape(3,4)

#scalar operation (single array)(all arithmetc operation)

p = a*2 # all operation is conduct ex..
print(p)

# relational operator

s = a>5 # all relational operator
print(s)

# vector operation(multiple array)

g = a + b # all operator
print(g)

