#!/usr/bin/python3
""" Starts a Flask Web Application """


from flask import Flask, render_template
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


@app.route("/python/", defaults={"text": "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python(text):
    """ Method returns a custom text after
    web app starts listening on 0.0.0.0:5000
    Arg:
        default text is "is cool"
    Return:
        “Python ” followed by the value of the
        text variable (replace _ with space)
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def show_number(n):
    """ Method returns a custom text after
    web app starts listening on 0.0.0.0:5000
    Arg:
        number to append to url
    Return:
        “n is a number" only if n is an integer
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def html_template(n):
    """ Method returns a HTML page after
    web app starts listening on 0.0.0.0:5000
    Arg:
        number to append to url and display on body
    Return:
        an HTML page
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def html_odd_or_even(n):
    """ Method returns a HTML page after
    web app starts listening on 0.0.0.0:5000
    Arg:
        number to append to url and display on body
    Return:
        an HTML page that determines whether n is
        odd or even
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)
