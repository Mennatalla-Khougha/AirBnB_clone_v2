#!/usr/bin/python3
"""use storage for fetching data from the storage engine"""
from flask import Flask, render_template
from models import storage
app = Flask("__name__")



@app.teardown_appcontext
def end_session():
    """remove the current SQLAlchemy"""
    storage.close()

@app.route("/states_list", strict_slashes=False)
def List_of_states():
    """display HTML page"""
    states = storage.all("State")
    return render_template("7-7-states_list.html", states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

