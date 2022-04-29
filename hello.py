from flask import Flask

app = Flask(__name__)


@app.route("/japan/<city>")
def japan(city):
    return f"<h1>Hello, {city} in Japan!</h1>"


html = """
<h1>見出し</h1>
<ul>
    <li>箇条書き1</li>
    <li>箇条書き2</li>
    <li>箇条書き3</li>
</ul>
"""


@app.route("/")
def hello():
    return html
