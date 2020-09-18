import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
height_weight = np.loadtxt('C:/User/heights.csv',delimiter=',')
x=height_weight[:,[0]]
y=height_weight[:,[1]]
line=LinearRegression()
line.fit(x,y)
print(line.coef_)
print(line.intercept_)
plt.plot(x,y,'o')
plt.plot(x,line.predict(x),'red')
plt.xlabel('height')
plt.ylabel('weight')
plt.show()