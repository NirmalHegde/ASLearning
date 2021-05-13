import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
import itertools
import os
import shutil
import random
import glob
import matplotlib.pyplot as plt
import warnings

path_All_Images = "Sign_Language_Letters/All_Images"

if os.path.isdir("Sign_Language_Letters/train/A") is False:
    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    for letter in letters:
        os.makedirs(f"Sign_Language_Letters/train/{letter}")
        os.makedirs(f"Sign_Language_Letters/valid/{letter}")
        os.makedirs(f"Sign_Language_Letters/test/{letter}")

        for file in random.sample(glob.glob(f"{path_All_Images}/{letter}*"), 500):
            shutil.move(file, f"Sign_Language_Letters/train/{letter}")

        for file in random.sample(glob.glob(f"{path_All_Images}/{letter}*"), 100):
            shutil.move(file, f"Sign_Language_Letters/valid/{letter}")

        for file in random.sample(glob.glob(f"{path_All_Images}/{letter}*"), 50):
            shutil.move(file, f"Sign_Language_Letters/test/{letter}")

train_path = "Sign_Language_Letters/train"
valid_path = "Sign_Language_Letters/valid"
test_path = "Sign_Language_Letters/test"

train_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input) \
    .flow_from_directory(directory=train_path, target_size=(224, 224),
                         classes=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                                  "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                                  "U", "V", "W", "X", "Y", "Z"],
                         batch_size=10)
valid_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input) \
    .flow_from_directory(directory=valid_path, target_size=(224, 224),
                         classes=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                                  "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                                  "U", "V", "W", "X", "Y", "Z"],
                         batch_size=10)
test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input) \
    .flow_from_directory(directory=test_path, target_size=(224, 224),
                         classes=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                                  "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                                  "U", "V", "W", "X", "Y", "Z"],
                         batch_size=10, shuffle=False)
images, labels = next(train_batches)

def plotImages(images_arr):
    fig, axes = plt.subplots(1, 10, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()


model = Sequential([
        Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same', input_shape=(224, 224, 3)),
        MaxPool2D(pool_size=(2, 2), strides=2),
        Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same'),
        MaxPool2D(pool_size=(2, 2), strides=2),
        Flatten(),
        Dense(units=26, activation='softmax')
])

model.compile(optimizer=Adam(learning_rate=0.001), loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(x=train_batches,
          steps_per_epoch=len(train_batches),
          validation_data=valid_batches,
          validation_steps=len(valid_batches),
          epochs=10,
          verbose=2)

