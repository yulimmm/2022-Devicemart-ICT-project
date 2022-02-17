#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense, Activation
#from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
#import numpy as np
#import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = mnist.load_data()
X_train = x_train.reshape(60000,784)
X_test = x_test.reshape(10000,784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
print("X Training matrix shape", X_train.shape)
print("X Testing matrix shape", X_test.shape)
