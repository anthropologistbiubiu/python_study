import tensorflow as tf
from tensorflow import keras
def build_model():
    model = keras.Sequential([keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    keras.layers.Dense(10, activation='softmax')])
    return model
model = build_model()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
