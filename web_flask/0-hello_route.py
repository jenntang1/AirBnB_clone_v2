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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
