# coding=utf-8

from __future__ import division, print_function
import numpy as np
import tensorflow as tf
import os
from keras import models
import cv2
from keras import backend as K
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

model = models.load_model('./siamese.h5', compile = False)
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
    print('hello')
    if model.predict((img1, img2))[0][0] <= 1.5:
        return "The Signature is likely to be Genuine"
    else:
        return "The Signature is likely to be Forged"

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
        print(f1)
        print(f2)
        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file1_path = os.path.join(
            basepath, 'uploads', secure_filename(f1.filename))
        f1.save(file1_path)
        file2_path = os.path.join(
            basepath, 'uploads', secure_filename(f2.filename))
        f2.save(file2_path)

        # Make prediction
        preds = check_forgery(file1_path, file2_path)
        return preds
    return None

if __name__ == '__main__':
    app.run(port=5001,debug=True)
