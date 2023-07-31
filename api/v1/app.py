#!/usr/bin/python3
from flask import Flask
import os

app = Flask(__name__)

from models import storage
from api.v1.views import app_views

app.register_blueprint(app_views)

@app.teardown_appcontext
def tear_down(exception):
    """method to handle teardown"""
    storage.close()

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    app.debug = True

    # Run the flask server
    app.run(host=host, port=port, threaded=True)
