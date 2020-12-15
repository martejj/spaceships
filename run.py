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
    return jsonify(l_ids=models.get_l_ids())

@app.route('/api/location/', methods=["DELETE"])
@validate_args(LIDSchema, 'location')
def remove_location(location):
    location.delete()
    return "Success"

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
    return jsonify(s_ids=models.get_s_ids())

@app.route('/api/spaceship/travel/', methods=["PUT"])
@validate_args(LIDSchema, 'location')
@validate_args(SIDSchema, 'spaceship')
def travel_ship(location, spaceship):
    spaceship.travel(location)
    return "Success"

@app.route('/api/spaceship/', methods=["DELETE"])
@validate_args(SIDSchema, 'spaceship')
def remove_spaceship(spaceship):
    spaceship.delete()
    return "Success"
