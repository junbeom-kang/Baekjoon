from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np


first_x=np.random.randint(100,size=(100,3))
second_x=np.random.randint(50,100,size=(100,3))

first_y=np.zeros(100).astype('int64')
first_y=first_y.reshape(100,1)
second_y=np.ones(100).astype('int64')
second_y=second_y.reshape(100,1)
X=np.concatenate((first_x,second_x),axis=0)
Y=np.concatenate((first_y,second_y),axis=0)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
model=LogisticRegression()
print(Y_test)
model.fit(X_train,Y_train)
Y_pred=model.predict(X_test)
accuracy_score(X_test, Y_pred)
