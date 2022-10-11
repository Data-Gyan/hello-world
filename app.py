import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Build:Entry-Point hit for the first flask app"

@app.route('/container')
def hello():
    return "<H1> Hello World ..!</H1>"

if __name__ == "__main__":
    app.run()


