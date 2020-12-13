from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/location/', methods=["POST"])
def post_location():

    return jsonify(id="uuid")

@app.route('/api/location/', methods=["GET"])
def get_location():

    return jsonify(id="uuid")

@app.route('/api/spaceship/', methods=["POST"])
def post_spaceship():

    return jsonify(id="uuid")

@app.route('/api/spaceship/', methods=["GET"])
def get_spaceship():

    return jsonify(name="Rocinante", model="MCRN Destroyer", location="l", status="Operational")