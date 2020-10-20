import matplotlib.pyplot as plt
import numpy as np
a=[1,3]
type(a)
head_width = 1.6
width = 0.001
plt.arrow(0, 0, 35.2 - head_width * 2, 16.3 - head_width * 2 + 1,
color = 'black',
width=width,
head_width=head_width)
plt.xlim(-40, 40)
plt.ylim(-40, 40)
plt.grid(True)
plt.xlabel('sugar')
plt.ylabel('moisture')
plt.title('Fruit Firgure')