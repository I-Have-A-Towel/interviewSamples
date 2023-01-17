from flask import Flask
from os import getenv, scandir

app = Flask(__name__)


@app.route("/")
def hello_world():
    files = scandir("/inputs")
    if len(files) == 0:
        raise Exception("No files!")

    text_1 = "Hello, World!"
    text_2 = f"My name is {getenv('NAME', 'unknown')}"
    text_3 = f"and I have {len(files)} files in /inputs"
    return f"{text_1} {text_2} {text_3}"
