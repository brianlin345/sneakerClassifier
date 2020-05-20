import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image


import numpy as np
import matplotlib.pyplot as plt


image_size = (125, 250)
h5_path = 'sneakerClassification/saved_models'
h5_file = 'shoe_model_class4.h5'
class_names = ['Jordan 1', 'Jordan 4', 'Jordan 11', 'Air Force 1']


def load_saved_model():
    loaded_model = tf.keras.models.load_model(os.path.join(h5_path, h5_file))
    return loaded_model

def predict_image(image_dir, image_name):
    loaded_model = load_saved_model()
    img = image.load_img(os.path.join(image_dir, image_name), target_size=(image_size[0], image_size[1]))

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    curr_image = np.vstack([img_array])

    prediction = np.argmax(loaded_model.predict(curr_image, batch_size=10), axis = -1)[0]
    return class_names[prediction]
