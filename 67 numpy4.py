# changing datatype

import numpy as np

a = np.arange(8).reshape(2,2,2)

p=a.astype(np.int32)
print(p.dtype)