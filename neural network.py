# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 11:53:33 2018
Edited by THAGracilamine
@author: 北海若
"""

import keras


def get_model():
    model = keras.models.Sequential()
    model.add(keras.layers.ConvLSTM2D(32, 6, strides=(2, 2), input_shape=(5, 80, 80, 3)))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.LeakyReLU())
    model.add(keras.layers.Conv2D(64, 5))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.LeakyReLU())
    model.add(keras.layers.Conv2D(64, 5, strides=(2, 2)))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.LeakyReLU())
    model.add(keras.layers.Conv2D(128, 5, strides=(2, 2)))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.LeakyReLU())
    model.add(keras.layers.Conv2D(256, 4))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.LeakyReLU())
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(256))
    model.add(keras.layers.LeakyReLU())
    model.add(keras.layers.Dense(128))
    model.add(keras.layers.Dense(8))
    model.add(keras.layers.Activation("softmax"))
    return model
