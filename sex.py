from sklearn.datasets import load_iris, load_breast_cancer # dataset
from sklearn.linear_model import LogisticRegression # 모델 생성
from sklearn.metrics import accuracy_score, confusion_matrix # 분류정확도, 교차분할표 : 모델 평가


breast = load_breast_cancer()
breast_x = breast.data
breast_y = breast.target  # 0 or 1 인 데이터
model = LogisticRegression()
model.fit(breast_x,breast_y)
y_pred = model.predict(breast_x)
acc = accuracy_score(breast_y, y_pred)
score = model.score(breast_x, breast_y)
print(score)
print('accuracy =', acc)