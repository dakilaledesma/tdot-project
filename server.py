from __future__ import print_function

import socket
socket.setdefaulttimeout(4000)

from flask import Flask, render_template, get_template_attribute
import pandas as pd
import flask

app = Flask(__name__)

precip_df = pd.read_csv("data/precip.dat", delimiter="  ", engine="python")
print(precip_df.head())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    pass

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, threaded=True, debug=False)
