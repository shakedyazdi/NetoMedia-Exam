# -*- coding: utf-8 -*-
from flask import Flask
from cpu_load_generator import load_all_cores

app = Flask(__name__)

@app.route("/")

def hello():
    return "Hello World!"

@app.route("/intense")
def intense():
    load_all_cores(duration_s=30, target_load=0.95)
    return "Got You!"

@app.route("/shaked")
def shaked():
    return "hello shaked"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

