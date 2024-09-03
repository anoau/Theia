
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Dropout, Activation, BatchNormalization
from keras.optimizers import SGD
from keras.initializers import RandomNormal
import tensorflow as tf
import keras
import numpy


(x_tr, y_tr), (x_te, y_te) = mnist.load_data()
print (x_tr.shape)

X_train = numpy.array([[1] * 128] * (10 ** 4) + [[0] * 128] * (10 ** 4))
X_test = numpy.array([[1] * 128] * (10 ** 2) + [[0] * 128] * (10 ** 2))

Y_train = numpy.array([True] * (10 ** 4) + [False] * (10 ** 4))
Y_test = numpy.array([True] * (10 ** 2) + [False] * (10 ** 2))
print(Y_train.shape)
X_train = X_train.astype("float32")
X_test = X_test.astype("float32")

Y_train = Y_train.astype("bool")
Y_test = Y_test.astype("bool")

batch_size =32
nb_epoch =0

model = Sequential()
model.add(Dense(units=50,activation='relu', input_dim=128))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Dense(units=50))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(1))
model.add(Activation('sigmoid'))
rms = keras.optimizers.RMSprop()

model.compile(loss='binary_crossentropy', optimizer=rms,metrics=['accuracy'])
model.fit(X_train, Y_train, batch_size=batch_size, epochs=20, verbose=1, validation_data=(X_test, Y_test))       


