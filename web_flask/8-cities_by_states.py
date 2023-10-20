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


@app.route("/cities_by_states", strict_slashes=False)
def List_of_states():
    """display HTML page"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
