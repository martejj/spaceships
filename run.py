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