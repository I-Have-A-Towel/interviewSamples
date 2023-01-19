from flask import Flask
from os import getenv, scandir

app = Flask(__name__)


@app.route("/")
def hello_world():
    files = scandir("/inputs")
    if len(files) == 0:
        raise Exception("No files!")

    name = getenv("NAME", None)
    if name is None:
        raise Exception("I don't know who I am!")

    text_1 = "Hello, World!"
    text_2 = f"My name is {name}"
    text_3 = f"and I have {len(files)} files in /inputs"
    return f"{text_1} {text_2} {text_3}"
