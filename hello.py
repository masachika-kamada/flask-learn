from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/japan/<city>")
def japan(city):
    return f"<h1>Hello, {city} in Japan!</h1>"


@app.route("/")
def hello():
    return render_template("hello.html")
