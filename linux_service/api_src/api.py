from flask import Flask
from os import getenv, scandir

app = Flask(__name__)


@app.route("/")
def hello_world():
    files = scandir("/inputs")
    return f"Hello, World! My name is {getenv('NAME', 'unknown')} and I have {len(files)} files in /inputs"
