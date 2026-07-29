from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
   return render_template("home.html")

@app.route("/frozen")
def frozen_in_time():
   return render_template("stories/frozen_in_time.html")

@app.route("/strike")
def strike_booth():
   return render_template("stories/strike_booth.html")

@app.route("/merch")
def merch():
    return render_template("merch.html")

