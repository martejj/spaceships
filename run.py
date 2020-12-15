from flask import Flask, jsonify, abort
from util import validate_args, validate_body
from schemata import SIDSchema, LIDSchema, SpaceshipPostSchema, SpaceshipUpdateSchema, LocationPostSchema, LocationUpdateSchema
import uuid
from pprint import pprint
import models

app = Flask(__name__)

locations = {}
spaceships = {}

@app.route('/')
def hello():
    return 'Hello, World!' 

'''
    /api/location endpoints
'''

@app.route('/api/location/', methods=["POST"])
@validate_body(LocationPostSchema, 'location')
def post_location(location):
    models.add_location(location)
    return jsonify(id=location.id)

@app.route('/api/location/', methods=["GET"])
@validate_args(LIDSchema, 'location')
def get_location(location):
    return location.get_json()
        

@app.route('/api/locations/', methods=["GET"])
def get_locations():
    l_ids = []
    for l_id in locations:
        l_ids.append(l_id)
    return jsonify(l_ids=l_ids)

@app.route('/api/location/', methods=["DELETE"])
@validate_args(LIDSchema, 'l_id_data')
def remove_location(l_id_data):
    pass

'''
    /api/spaceship endpoints
'''

@app.route('/api/spaceship/', methods=["POST"])
@validate_body(SpaceshipPostSchema, 'spaceship')
def post_spaceship(spaceship):
    models.add_spaceship(spaceship)
    return jsonify(id=spaceship.id)

@app.route('/api/spaceship/', methods=["GET"])
@validate_args(SIDSchema, 'spaceship')
def get_spaceship(spaceship):
    return spaceship.get_json()

@app.route('/api/spaceships/', methods=["GET"])
def get_spaceships():
    s_ids = []
    for s_id in spaceships:
        s_ids.append(s_id)
    return jsonify(s_ids=s_ids)

@app.route('/api/spaceship/travel/', methods=["PUT"])
@validate_args(LIDSchema, 'l_id_data')
@validate_args(SIDSchema, 's_id_data')
def travel_ship(l_id_data, s_id_data):
    pass

@app.route('/api/spaceship/', methods=["DELETE"])
@validate_args(SIDSchema, 's_id_data')
def remove_spaceship(s_id_data):
    if not s_id_data in spaceships:
        abort(400, "Invalid s_id: Spaceship does not exist")
    spaceship = spaceships[s_id_data]

