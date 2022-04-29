from flask import Flask

app = Flask(__name__)


@app.route("/japan/tokyo")
def japan():
    return "<p>Hello, tokyo in Japan!</p>"


@app.route("/japan/nara")
def nara():
    return "<p>Hello, nara in Japan!</p>"


@app.route("/japan/saitama")
def saitama():
    return "<p>Hello, saitama in Japan!</p>"
