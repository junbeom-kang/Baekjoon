import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
import numpy as np
digits = load_digits(n_class=6)
print(digits)
print(digits.feature_names)
one_idx = np.argwhere(digits.target ==1)
fig,ax = plt.subplots(5, 5, figsize=(6, 6))
j = 1
one_idx=list(map(int,one_idx))

for i in one_idx:
    plt.subplot(5,5,j)
    for temp in digits.images[i][1:7]:
        print(temp[2:6])
    plt.imshow(digits.images[i],cmap='binary')
    j+=1
    print()
    if j>25:
        break
plt.show()

