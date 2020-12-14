from flask import Flask, jsonify
from util import validate_args, validate_body
from schemata import SIDSchema, LIDSchema, SpaceshipPostSchema, SpaceshipUpdateSchema, LocationPostSchema, LocationUpdateSchema
import uuid

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!' 

@app.route('/api/location/', methods=["POST"])
@validate_body(LocationPostSchema)
def post_location(data):
    return jsonify(id=uuid.uuid4().hex)

@app.route('/api/location/', methods=["GET"])
@validate_args(LIDSchema)
def get_location(args_data):
    return jsonify(name="Naval Yard", planet="Earth", capacity=1)

@app.route('/api/spaceship/', methods=["POST"])
@validate_body(SpaceshipPostSchema)
def post_spaceship(data):
    return jsonify(id=uuid.uuid4().hex)

@app.route('/api/spaceship/', methods=["GET"])
@validate_args(SIDSchema)
def get_spaceship(args_data):
    return jsonify(name="Rocinante", model="MCRN Destroyer", location="l", status="Operational")

@api.route('/api/locations/', methods=["GET"])
def get_locations():
    return jsonify(l_ids=[uuid.uuid4().hex, uuid.uuid4().hex])

@api.route('/api/locations/', methods=["GET"])
def get_locations():
    return jsonify(l_ids=[uuid.uuid4().hex, uuid.uuid4().hex])

@api.route('/api/spaceship/travel/', methods=["PUT"])
@validate_args(LIDSchema, 'l_id_data')
@validate_args(SIDSchema, 's_id_data')
def travel_ship(l_id_data, s_id_data):
    pass

@api.route('/api/location/', methods=["DELETE"])
@validate_args(LIDSchema, 'l_id_data')
def remove_location(l_id_data):
    pass

@api.route('/api/spaceship/', methods=["DELETE"])
@validate_args(SIDSchema, 's_id_data')
def remove_location(s_id_data):
    pass

