from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
import numpy as np
#import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = mnist.load_data()
X_train = x_train.reshape(60000,784)
X_test = x_test.reshape(10000,784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

Y_train = to_categorical(y_train,10)
Y_test = to_categorical(y_test,10)

model = Sequential() #인공지능 모델을 시퀀셜 방식으로 개발
model.add(Dense(512, input_shape=(784,))) #입력받는 데이터 형태: 784, 해당 은닉층 모델: 512
model.add(Activation('relu')) #다음층으로 값을 전달할 때 렐루 함수 사용
model.add(Dense(256))#다음층을 추가. 두 번째 은닉층은 256개의 노드로 구성. 두 번째 은닉층부터는 입력받는 노드를 설정할 필요 x 
model.add(Activation('relu'))#역시 렐루 방식으로 값 전달
model.add(Dense(10))#마지막 층은 10개 노드로
model.add(Activation('softmax'))# 각 노드에서 전달되는 값의 총 합이 1이 되도록 소프트맥스 함수를 사용
#model.summary() #summary 함수는 모델이 어떻게 구성되었는지 살펴보는 함수

model.compile(loss='categorical_crossentropy', optimizer = 'adam',metrics=['accuracy'])
model.fit(X_train, Y_train, batch_size=128, epochs = 10, verbose=1) #한번에 128개의 데이터를 학습하고, 한 데이터당 10번씩 학습하기

score = model.evaluate(X_test, Y_test)
print('Test Lose:',score[0])
print('Test accuracy:',score[1])

predicted_classes = np.argmax(model.predict(X_test),axis=1)
correct_indices = np.nonzero(predicted_classes == y_test)[0]  #맞은 값 구분
incorrect_indices = np.nonzero(predicted_classes != y_test)[0]  #틀린 값 구분
