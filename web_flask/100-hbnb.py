#!/usr/bin/python3
"""use storage for fetching data from the storage engine"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.user import User
app = Flask(__name__)


@app.teardown_appcontext
def end_session(exception):
    """remove the current SQLAlchemy"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def index():
    """display am HTML page"""
    states = storage.all(State).values()
    amenities=storage.all(Amenity).values()
    users = storage.all(User).values()
    return render_template("100-hbnb.html", states=states, amenities=amenities, users=users)


if __name__ == "__main__":
    app.run(host='0.0.0.0')