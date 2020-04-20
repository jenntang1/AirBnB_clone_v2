#!/usr/bin/python3
""" Starts a Flask Web Application """


from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Method returns a hello message after
    web app starts listening on 0.0.0.0:5000
    Return:
        “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Method returns a custom message after
    web app starts listening on 0.0.0.0:5000
    Return:
        “HBNB”
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_c(text):
    """ Method returns a custom text after
    web app starts listening on 0.0.0.0:5000
    Arg:
        text to append to url
    Return:
        “C ” followed by the value of the
        text variable (replace _ with space)
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
