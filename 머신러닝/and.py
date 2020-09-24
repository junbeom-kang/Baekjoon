from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
iris = load_iris()
idx = np.in1d(iris.target, [0, 2])
X = iris.data[idx, :2]
y = (iris.target[idx] / 2).astype(np.int)
model = Perceptron(max_iter=300, shuffle=False, tol=0, n_iter_no_change=1e9).fit(X, y)
XX_min = X[:, 0].min() - 1
XX_max = X[:, 0].max() + 1
YY_min = X[:, 1].min() - 1
YY_max = X[:, 1].max() + 1
XX, YY = np.meshgrid(np.linspace(XX_min, XX_max, 1000),
np.linspace(YY_min, YY_max, 1000))
ZZ = model.predict(np.c_[XX.ravel(), YY.ravel()]).reshape(XX.shape)
plt.contourf(XX, YY, ZZ, cmap=mpl.cm.autumn)
plt.scatter(X[y == 0, 0], X[y == 0, 1], c='w', s=100, marker='o', edgecolor='k')
plt.scatter(X[y == 1, 0], X[y == 1, 1], c='k', s=100, marker='x', edgecolor='k')
plt.xlabel("꽃받침의 길이")
plt.ylabel("꽃받침의 폭")
plt.title("붓꽃 데이터(setosa/virginica)")
plt.xlim(XX_min, XX_max)
plt.ylim(YY_min, YY_max)
plt.grid(False)
plt.show()