#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def get_status():
    """
    Function that returns status Ok
    return the response in json format
    """
    response = {
        "status": "OK"
    }
    return jsonify(response)
