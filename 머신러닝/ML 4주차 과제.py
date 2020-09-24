import matplotlib.pylab as plt
#matplotlib.pylab모듈을 plt로 축약하여 불러온다
import numpy as np
#numpy모듈도 np로 축약하여 불러온다
from sklearn.linear_model import LinearRegression
#sklearn.linear_model에서 선형회귀모듈을 불러온다
from sklearn import datasets
#싸이킷런의 datasets모듈을 불러온다
from sklearn.model_selection import train_test_split
#sklearn.model_selection의 train_test_split모듈을 불러온다
diabetes = datasets.load_diabetes()
#당뇨병 데이터를 불러와서 diabets에 저장합니다
diabetes_X_train = diabetes.data[:-20,:]
#diabetes_X_train을 diabetes의 데이터행렬에서 뒤에서 20번째인 행 전까지의 모든행과  모든열을 저장한다
diabetes_X_test = diabetes.data[-20:,:]
#diabetes X test에는 뒤에서 20번째 행부터 마지막행까지와  모든열을 저장한다
diabetes_y_train = diabetes.target[:-20]
#diabetes_y_train는 diabetes의 타깃행렬에서 처음부터 뒤에서 20번째 전까지의 타깃값을 저장한다
diabetes_y_test = diabetes.target[-20:]
#diabetes_y_test에는 diabetes의 타깃행렬 뒤에서20번째부터 마지막까지의 타깃값을 저장한다
model = LinearRegression()
#model에 선형회귀모델을 생성합니다
model.fit(diabetes_X_train, diabetes_y_train)
#model값에 diabetes_X_train, diabetes_y_train변수를 fit시킵니다(train값들로 훈련시키기위해)
y_pred = model.predict(diabetes_X_test)
#y_pred에 model.fit에서 만들어진 값들을 이용해서 x값에 diabetes_X_test값이 들어왔을때의 값을 예측한값을 넣는다.
plt.plot(diabetes_y_test, y_pred, '.')
#그림을 그리위해서 plot의 첫번째에 y_test값을
x = np.linspace(0, 330, 100)
#x를 0~330까지 100개로 나눠서 저장한
y = x
#y=x그래프를 만들기위해 y=x
plt.plot(x, y,'r')
#그림을 그리위해 plot에 x,y를 넣는다
plt.show()
#그림을 보여준다