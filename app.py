from flask import Flask
from flask import render_template

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "hello world"

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/frozen")
def frozen_in_time():
   return render_template("frozen_in_time.html")