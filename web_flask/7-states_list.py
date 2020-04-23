#!/usr/bin/python3
""" Starts a Flask Web Application """


from models.state import State
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


def get_data(self):
    """ Method fetches data from storage
    """
    data = storage.all(State)


@app.route("/states_list", strict_slashes=False)
def html_states(self):
    """ Method returns a HTML page after
    web app starts listening on 0.0.0.0:5000
    Return:
        an HTML page that States and their ids
    """
    data = get_data()
    return render_template("7-states_list.html", data=data)


@app.teardown_appcontext
def close_db(self):
    """ Method closes the database
    Arg:
        storage data
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
