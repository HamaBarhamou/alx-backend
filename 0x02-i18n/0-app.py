#!/usr/bin/env python3
""" 0x02. i18n """
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('0-index.html')
