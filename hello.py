from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/japan/<city>")
def japan(city):
    return render_template("hello.html", city=city)


@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"
