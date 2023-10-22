#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

# Import necessary modules and classes
from flask import Flask, render_template
from models import *
from models import storage

# Create a Flask web application instance
app = Flask(__name__)

# Define routes for '/states' and '/states/<state_id>'
@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
    This function displays the states and cities listed in alphabetical order.
    It retrieves states from the storage and optionally filters by 'state_id'.
    """
    # Retrieve all states from the storage
    states = storage.all("State")
    
    # If 'state_id' is provided, modify it for query purposes
    if state_id is not None:
        state_id = 'State.' + state_id
    
    # Render the '9-states.html' template and pass states and state_id to it
    return render_template('9-states.html', states=states, state_id=state_id)

# Define a teardown function for the Flask app context
@app.teardown_appcontext
def teardown_db(exception):
    """
    This function closes the storage when the Flask app context is torn down.
    It ensures that the storage is properly closed when the application is done.
    """
    storage.close()

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
