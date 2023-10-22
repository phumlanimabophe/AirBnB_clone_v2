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

# Define a route for '/hbnb_filters'
@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    # Retrieve states and amenities from the storage
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    
    # Render the '10-hbnb_filters.html' template and pass the states and amenities to it
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

# Define a teardown function for the Flask app context
@app.teardown_appcontext
def teardown_db(exception):
    # Close the storage when the Flask app context is torn down
    storage.close()

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
