import numpy as np
import random
data=np.array([1,2,3,4,5,6,7])
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(names=='Bob')
print(data[names=='Bob'])