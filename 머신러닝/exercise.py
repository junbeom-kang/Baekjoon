import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


x=np.random.randn(100,1)*10
y=x+np.random.randn(100,1)+5
line=LinearRegression()
line.fit(x,y)
pred_y=line.predict(x)
print(line.coef_)
print(line.intercept_)
plt.plot(x,y,'o')
plt.plot(x,pred_y)
plt.show()