#!/usr/bin/python3
""" Starts a Flask Web Application """


from models.state import State
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def html_cities():
    """ Method returns a HTML page after
    web app starts listening on 0.0.0.0:5000
    Return:
        an HTML page that displays the cities data
    """
    data = storage.all(State)
    states = data.values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_db(self):
    """ Method closes the database
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
