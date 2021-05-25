from __future__ import print_function

import socket
socket.setdefaulttimeout(4000)

from flask import Flask, render_template, get_template_attribute
import flask

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, threaded=True, debug=False)
