from flask import Flask
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/forgery')
def forgery():
    return render_template('forgery.html')

@app.route('/detection')
def detection():
    return render_template('detection.html')