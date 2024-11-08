from flask import Flask, redirect, render_template
from config import *



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

app.run(debug=True)