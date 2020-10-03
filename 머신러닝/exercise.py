import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
# 0 : 양성, 1 : 악성
label_dict = {'M':0, 'B':1}
dataset = pd.read_csv('C:/data.csv')
dataset = dataset.drop('id', axis=1) # 필요 없는 데이터 삭제
dataset['diagnosis'] = dataset['diagnosis'].map(label_dict) # 라벨 맵핑
dataset.shape
data_label = dataset['diagnosis']
data_feature = dataset.drop('diagnosis', axis=1)
split = int(len(data_feature) * 0.8)
train_feature = data_feature[:split]
train_label = data_label[:split]
test_feature = data_feature[split:]
test_label = data_label[split:]
model = LogisticRegression(max_iter=10000)
model.fit(train_feature, train_label)
pred = model.predict(test_feature)
accuracy_score(test_label, pred)