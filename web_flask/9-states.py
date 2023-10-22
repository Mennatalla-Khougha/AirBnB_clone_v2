#!/usr/bin/python3
"""use storage for fetching data from the storage engine"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def end_session(exception):
    """remove the current SQLAlchemy"""
    storage.close()


@app.route("/states", strict_slashes=False)
def List_of_states(id=None):
    """display HTML page"""
    state = storage.all(State)
    return render_template("9-states.html", state=state, id=None)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """display HTML page"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
