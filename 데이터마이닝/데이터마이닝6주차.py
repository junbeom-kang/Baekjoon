from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
iris = load_iris()
temp=np.concatenate((iris.data,iris.target.reshape(150,1)),axis=1)
temp=np.concatenate((temp,np.zeros(shape=(150,1))),axis=1)
frame=pd.DataFrame(temp,columns=[iris.feature_names+['target','targetName']])
frame.iloc[:,5]=np.where(frame.iloc[:,4]==0,'setosa',np.where(frame.iloc[:,4]==1,'versicolor','virginica'))

plt.figure()
plt.scatter(frame.iloc[:50,0],frame.iloc[:50,1],marker='o',c='red',label='setosa')
plt.scatter(frame.iloc[50:100,0],frame.iloc[50:100,1],marker='x',c='blue',label='versicolor')
plt.scatter(frame.iloc[100:150,0],frame.iloc[100:150,1],marker='^',c='green',label='virginica')
plt.legend()
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()
plt.figure()
plt.scatter(frame.iloc[:50,2],frame.iloc[:50,3],marker='o',c='red',label='setosa')
plt.scatter(frame.iloc[50:100,2],frame.iloc[50:100,3],marker='x',c='blue',label='versicolor')
plt.scatter(frame.iloc[100:150,2],frame.iloc[100:150,3],marker='^',c='green',label='virginica')
plt.legend()
plt.xlabel('petal length')
plt.ylabel('pepal width')
plt.show()