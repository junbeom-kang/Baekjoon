from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
# Load the iris dataset
iris = datasets.load_iris()
# Create our X and y data
X = iris.data
y = iris.target
print(X)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(X_train.shape)
print(y_train.shape)
sc = StandardScaler() #StandardScaler를 X_train 데이터가 mean = 0, variance = 1로 만들 수 있도록 학
sc.fit(X_train)
# Apply the scaler to the X training data
X_train_std = sc.transform(X_train)
# Apply the SAME scaler to the X test data
X_test_std = sc.transform(X_test)
# Create a perceptron object with the parameters: 40 iterations (epochs) over the data, and a learning

ppn = Perceptron()
# Train the perceptron
ppn.fit(X_train_std, y_train)
y_pred = ppn.predict(X_test_std)
