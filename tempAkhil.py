
from __future__ import division, print_function
# coding=utf-8
import sys
import glob
import re
import numpy as np
import tensorflow as tf
from tensorflow import keras

# from tf.compat.v1 import ConfigProto
# from tensorflow.compat.v1 import InteractiveSession
import os
from keras import models
import cv2
from keras import backend as K


model = models.load_model('siamese.h5', compile = False)
def check_forgery(path_img_1, path_img_2):
    img1 = cv2.imread(path_img_1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(path_img_2, cv2.IMREAD_GRAYSCALE)
    img1 = cv2.resize(img1, dsize=(155, 220))
    img2 = cv2.resize(img2, dsize=(155, 220))
    print(img1.shape)
    img1 = img1.astype('int32')
    img2 = img2.astype('int32')
    img1 = img1.reshape((1, 155, 220, 1))
    img2 = img2.reshape((1, 155, 220, 1))
    
    if model.predict((img1, img2))[0][0] <= 1.5:
        return True
    else:
        return False
# config = ConfigProto()
# config.gpu_options.per_process_gpu_memory_fraction = 0.2
# config.gpu_options.allow_growth = True
# session = tf.compat.v1.InteractiveSession(config=config)
# # Keras

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f1 = request.files['file1']
        f2 = request.files['file2']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f1.filename))
        f1.save(file_path)

        # Make prediction
        preds = check_forgery(f1, f2)
        return preds
    return None


if __name__ == '__main__':
    app.run(port=5001,debug=True)
