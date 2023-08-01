#!/usr/bin/python3
"""
    flask with general routes
    routes:
        /status:    display "status":"OK"
        /stats:     dispaly total for all classes
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """
    Function that returns status Ok
    return the response in json format
    """
    response = {
        "status": "OK"
    }
    return jsonify(response)


@app_views.route('/stats')
def stats():
    """
    End point that retrieves number of object
    """
    obj = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return (jsonify(obj))
