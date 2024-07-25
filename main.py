import os
from flask import Flask, session, url_for, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/lenticel')
def lenticel():
    #return redirect("https://lenticel.onrender.com")
    return render_template("lenticel.html")

@app.route('/harmony')
def harmony():
    return render_template("harmony.html")

@app.route('/bulletin')
def bulletin():
    return render_template("bulletin.html")

@app.route('/set')
def set():
    return render_template("set.html")
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)