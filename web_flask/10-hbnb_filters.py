#!/usr/bin/python3
"""use storage for fetching data from the storage engine"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def end_session(exception):
    """remove the current SQLAlchemy"""
    storage.close()


@app.route("/hbnb_filters")
def index():
    """display am HTML page"""
    states = storage.all(State)
    amenities=storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)