from flask import Flask, jsonify, abort
from util import validate_args, validate_body
from schemata import SIDSchema, LIDSchema, SpaceshipPostSchema, SpaceshipUpdateSchema, LocationPostSchema, LocationUpdateSchema
import uuid
from pprint import pprint

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
@validate_body(LocationPostSchema)
def post_location(data):
    data['id'] = uuid.uuid4().hex
    data['num_spaceships'] = 0
    data['spaceships'] = []
    locations[data['id']] = data
    return jsonify(id=data['id'])

@app.route('/api/location/', methods=["GET"])
@validate_args(LIDSchema)
def get_location(args_data):
    uuid = args_data['l_id']
    if uuid in locations:
        return jsonify(locations[uuid])
    abort(400, "Invalid l_id: Location does not exist")
        

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
@validate_body(SpaceshipPostSchema)
def post_spaceship(data):
    
    if not data['l_id'] in locations:
        abort(400, "Invalid l_id: Location does not exist")

    location = locations[data['l_id']]
    # If capacity add it.
    print(location['num_spaceships'])
    print(location['capacity'])
    if location['num_spaceships'] < location['capacity']:
        data['id'] = uuid.uuid4().hex
        spaceships[data['id']] = data
        location['num_spaceships'] += 1
        location['spaceships'].append(data['id'])
        return jsonify(id=data['id'])
    else:
        abort(400, "Location is at capacity")

@app.route('/api/spaceship/', methods=["GET"])
@validate_args(SIDSchema)
def get_spaceship(args_data):
    uuid = args_data['s_id']
    if uuid in spaceships:
        return jsonify(spaceships[uuid])
    abort(400, "Invalid s_id: Spaceship does not exist")

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

