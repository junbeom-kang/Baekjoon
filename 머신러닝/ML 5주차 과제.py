from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

#데이터 만들기
first=np.random.randint(100,size=(100,3))
first=np.concatenate((first,np.zeros(100,dtype='int32').reshape(100,1)),axis=1)
second=np.random.randint(50,100,size=(100,3))
second=np.concatenate((second,np.ones(100,dtype='int32').reshape(100,1)),axis=1)
#데이터 합치기
newdata=np.concatenate((first,second),axis=0)
#데이터 x부분과 y부분 분리하기
X=newdata[:,:3]
y=newdata[:,3].reshape(-1)
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3)
#로지스틱 리그레션모델 만들기
model = LogisticRegression()
model.fit(X_train, Y_train)
y_pred = model.predict(X_test)
print(model.score(X_test,y_pred))
