#!/usr/bin/python3
"""Script create a folder"""
from flask import Flask, jsonify
import os
from models import storage
from api.v1.views import app_views


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(exception):
    """method to handle teardown"""
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """
    A handler for 404 errors
    """
    response = {
        "error": "Not found"
    }
    return jsonify(response), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', 5000)

    app.debug = True

    # Run the flask server
    app.run(host=host, port=port, threaded=True)
