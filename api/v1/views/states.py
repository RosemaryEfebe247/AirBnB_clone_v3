#!/usr/bin/python3
"""
A view that handles all default RESTFul API(request) for State
HAndles the GET,POST< DELETE and PUT request
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'])
def state():
    """Route that retrieves all states objects"""
    states = storage.all(State)
    state_list = []
    for key, value in states.items():
        state_list.append(value.to_dict())
    return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET'])
def state_get(state_id):
    """Route that retrieves state with id"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def state_del(state_id):
    """Deletes the state linked to the id"""
    state = storage.get(State, state_id)
    if state is not None:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states/', methods=['POST'])
def state_post():
    """Create new state obj"""
    try:
        data = request.get_json()
        if not data:
            abort(400, 'Not a JSON')
        if 'name' not in data:
            abort(400, 'Missing name')
        state = State(**data)
        storage.new(state)
        storage.save()
    except Exception:
        abort(400)
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def state_put(state_id):
    """Update state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
