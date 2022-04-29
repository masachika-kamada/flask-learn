from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/japan/<city>")
def japan(city):
    return render_template("hello.html", city=city)


bullets = [
    "項目1",
    "項目2",
    "項目3",
    "項目4"
]


@app.route("/")
def hello():
    return render_template("bullet.html", bullets=bullets)
