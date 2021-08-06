from __future__ import print_function

import socket
socket.setdefaulttimeout(4000)

from flask import Flask, render_template, get_template_attribute
import pandas as pd

app = Flask(__name__)

precip_df = pd.read_csv("data/precip.dat", delimiter="  ", engine="python")
print(precip_df.head())

option_df = pd.read_excel("data/Spreadsheet for check5-17-2021.xlsx")
headings = [str(o) for o in option_df.iloc[1]]
option_df = option_df.rename(columns=option_df.iloc[2]).drop(option_df.index[2]).drop(option_df.index[1]).drop(option_df.index[0])



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loadoptions')
def options():
    options_html = ""

    last_heading = ""
    for idx, option_column in enumerate(option_df.columns):
        if str(option_column) != 'nan':
            try:
                _options = [str(o) for o in option_df[option_column].unique()]

                if headings[idx] != 'nan':
                    options_html += f"<h2>{headings[idx]}</h2>"

                if 'nan' in _options:
                    _options.remove('nan')
                    _options.sort()
                    _options.append('N/A')
                else:
                    _options.sort()


                options_html += f"""
                <p>{option_column}: 
                    <select class="search_select" id="{option_column.replace(' ', '')}">
                        {''.join([f'<option class="search_option" value="{o.replace(" ", "")}">{o}</option>' for o in _options])}
                    </select>
                """
            except AttributeError:
                print(option_column)

    return options_html


@app.route('/predict')
def predict():
    pass

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, threaded=True, debug=False)
