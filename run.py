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
    ########################## /api/location endpoints ########################################
'''

'''
    Creates a location with the given LocationPostSchema, for example:
    {
        name: "Mars dockyards",
        planet: "Mars",
        capacity: "1",
    }
    Returns the id of the location.
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
    
'''
    Gets all locations in the system.
    Returns the ids of the locations.
    {
        l_ids: [id1, id2, id3, ...]
    }
'''
@app.route('/api/locations/', methods=["GET"])
def get_locations():
    return jsonify(l_ids=models.get_l_ids())

'''
    Gets the location with the given l_id, taken in from the parameters.
    Returns the info of the location, for example:
    {
        name: "Mars dockyards",
        planet: "Mars",
        capacity: "1",
        num_spaceship: "0",
        s_ids: []
    }
'''
@app.route('/api/location/', methods=["DELETE"])
@validate_args(LIDSchema, 'location')
def remove_location(location):
    location.delete()
    return "Success"

'''
    ########################## /api/spaceship endpoints ########################################
'''

'''
    Creates a spaceship with the given SpaceshipPostSchema, for example:
    {
        name: "Rocinante",
        l_id: "uuid4",
        model: "MCRN Destroyer",
        status: "Decommissioned" | "Maintenance" | "Operational"
    }
    Returns the id of the spaceship.
'''
@app.route('/api/spaceship/', methods=["POST"])
@validate_body(SpaceshipPostSchema, 'spaceship')
def post_spaceship(spaceship):
    models.add_spaceship(spaceship)
    return jsonify(id=spaceship.id)

'''
    Gets the spaceship with the given s_id, taken in from the parameters.
    Returns the info of the spaceship, for example:
    {
        name: "Rocinante",
        l_id: "uuid4",
        model: "MCRN Destroyer",
        status: "Decommissioned" | "Maintenance" | "Operational"
    }
'''
@app.route('/api/spaceship/', methods=["GET"])
@validate_args(SIDSchema, 'spaceship')
def get_spaceship(spaceship):
    return spaceship.get_json()

'''
    Gets all spaceships in the system.
    Returns the ids of the spaceships.
    {
        s_ids: [id1, id2, id3, ...]
    }
'''
@app.route('/api/spaceships/', methods=["GET"])
def get_spaceships():
    return jsonify(s_ids=models.get_s_ids())

'''
    Takes in l_id and s_id and makes s_id travel to l_id if:
    - The spaceship status is operational.
    - The destination location is not full.
    Returns 200 on success or 400 on failure.
'''
@app.route('/api/spaceship/travel/', methods=["PUT"])
@validate_args(LIDSchema, 'location')
@validate_args(SIDSchema, 'spaceship')
def travel_ship(location, spaceship):
    spaceship.travel(location)
    return "Success"

'''
    Deletes the spaceship given in the s_id parameter.
'''
@app.route('/api/spaceship/', methods=["DELETE"])
@validate_args(SIDSchema, 'spaceship')
def remove_spaceship(spaceship):
    spaceship.delete()
    return "Success"

'''
    Updates the spaceship given in the s_id parameter with the information given in the body.
'''
@app.route('/api/spaceship/', methods=["PATCH"])
@validate_args(SIDSchema, 'spaceship')
@validate_body(SpaceshipUpdateSchema)
def update_spaceship(spaceship, data):
    spaceship.update(data)
    return "Success"