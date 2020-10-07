import sys
assert sys.version_info >= (3, 5)
from tensorflow import keras
import sklearn
assert sklearn.__version__ >= "0.20"
import tensorflow as tf
assert tf.__version__ >= "2.0"
import numpy as np
import tensorflow as tf
import pandas as pd
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

#데이터를 받아와서 valid와 train을 분류한다. 강의에서는 5000개로 valid를 정했지만 train크기의 1/10정도를 하시는것 같아서
#train이 1257개라서 125로 임의로 설정하였습니다.
digits = load_digits()
x_data = digits.data
y_data = digits.target
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3)
x_valid, x_train = x_train[:125], x_train[125:]
y_valid, y_train = y_train[:125], y_train[125:]
#plt.imshow(x_train[0].reshape(8,8),cmap='binary')

#행과열을 1,10으로 설정해서 test의 맨앞 10개를 볼수있도록 설정
class_names = [0,1,2,3,4,5,6,7,8,9]
n_rows = 1
n_cols = 10
plt.figure(figsize=(n_cols * 1.2, n_rows * 1.2))
for row in range(n_rows):
    for col in range(n_cols):
        index = n_cols * row + col
        plt.subplot(n_rows, n_cols, index + 1)
        plt.imshow(x_test[index].reshape(8,8), cmap="binary", interpolation="nearest")
        plt.axis('off')
        plt.title(class_names[y_test[index]], fontsize=12)
plt.subplots_adjust(wspace=0.2, hspace=0.5)
plt.show()

#sequential모델을 만듬
model = keras.models.Sequential([
keras.layers.Flatten(input_shape=[8, 8]),
keras.layers.Dense(300, activation="relu"),
keras.layers.Dense(100, activation="relu"),
keras.layers.Dense(10, activation="softmax")
])

#hidden1 = model.layers[1]
#weights, biases = hidden1.get_weights()

#갖고있는 트레이닝모델로 30번을 돌려보면서 확인
model.compile(loss="sparse_categorical_crossentropy",optimizer="sgd",metrics=["accuracy"])
tb_hist = keras.callbacks.TensorBoard(log_dir='./graph', histogram_freq=0, write_graph=True, write_images=True)
history = model.fit(x_train, y_train, epochs=30,validation_data=(x_valid, y_valid),callbacks=[tb_hist])