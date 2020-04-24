#!/usr/bin/python3
""" Starts a Flask Web Application """


from models.state import State
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def html_states_state():
    """ Method returns a HTML page after
    web app starts listening on 0.0.0.0:5000
    Return:
        an HTML page that displays city data by
        state
    """
    data = storage.all(State)
    if id:
        id = "State." + id
    return render_template("9-states.html", states=states, id=id)


@app.teardown_appcontext
def close_db(self):
    """ Method closes the database
    Arg:
        storage data
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
