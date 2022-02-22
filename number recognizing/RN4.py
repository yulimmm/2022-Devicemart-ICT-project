#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense, Activation
#from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
#import numpy as np
#import matplotlib.pyplot as plt

Y_train = to_categorical(y_train,10)
Y_test = to_categorical(y_test,10)
print("Y Training matrix shape", Y_train.shape)
print("Y Testing matrix shape", Y_test.shape)
