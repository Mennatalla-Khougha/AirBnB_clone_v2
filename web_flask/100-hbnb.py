#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.user import User
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(exception):
    "close storage"
    storage.close()


@app.route('/hbnb')
def hbnb():
    "displays a HTML page"
    return render_template(
        '100-hbnb.html',
        states=storage.all(State).values(),
        amenities_list=storage.all(Amenity).values(),
        users=storage.all(User).values()
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')