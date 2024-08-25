import tensorflow as tf
from tensorflow import keras
import numpy as np



(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
batch_size = 128
# Scaling data
x_train = x_train/255
x_test = x_test/255
# y_train = y_train/255
#reshape the data
x_train = x_train.reshape(60000,28,28,1)
x_test = x_test.reshape(10000,28,28,1)
y_train = y_train.reshape(60000,1)
y_test = y_test.reshape(10000,1)

#Create a model
model = keras.Sequential([
keras.layers.Conv2D(64,(3,3),(1,1),padding = "same", activation='relu', input_shape=(28,28,1)),
keras.layers.BatchNormalization(),
keras.layers.Dropout(0.2),
keras.layers.MaxPooling2D(pool_size = (2,2),padding = "valid"),
keras.layers.Conv2D(64,(3,3),(1,1),padding = "same",activation='relu'),
keras.layers.BatchNormalization(),
keras.layers.Dropout(0.2),
keras.layers.MaxPooling2D(pool_size = (2,2),padding = "valid"),
keras.layers.Flatten(),
keras.layers.Dense(128,activation = "relu"),
keras.layers.BatchNormalization(),
keras.layers.Dropout(0.2),
keras.layers.Dense(10,activation = "softmax")])

model.compile(optimizer = "adam",
loss = "sparse_categorical_crossentropy",
metrics  = ['accuracy'])

model.fit(x_train,y_train,epochs=10)
test_loss,test_acc = model.evaluate(x_test,y_test)
print("\ntest accuracy:",test_acc)