from flask import Flask
from os import getenv, scandir

app = Flask(__name__)

input_dir = getenv("INPUT_DIR", None)
files = scandir(input_dir)
if len(files) == 0:
    raise Exception("No files!")

name = getenv("NAME", None)
if name is None:
    raise Exception("I don't know who I am!")


@app.route("/")
def hello_world():
    text_1 = "Hello, World!"
    text_2 = f"My name is {name}"
    text_3 = f"and I have {len(files)} files in {input_dir}"
    return f"{text_1} {text_2} {text_3}"
