from marshmallow import Schema, fields, ValidationError, validates, validate, EXCLUDE, post_load
from models import locations, spaceships, Spaceship, Location
from flask import abort
import uuid

# Regex from https://stackoverflow.com/questions/7905929/how-to-test-valid-uuid-guid
# Dont use inbuilt UUID otherwise it parses the string weirdly. (e.g. inserts -'s)
s_id_required = fields.Str(required=True, validate=validate.Regexp('^[0-9a-f]{8}[0-9a-f]{4}[0-5][0-9a-f]{3}[089ab][0-9a-f]{3}[0-9a-f]{12}$', error="Malformed UUID"))
s_id = fields.Str(validate=validate.Regexp('^[0-9a-f]{8}[0-9a-f]{4}[0-5][0-9a-f]{3}[089ab][0-9a-f]{3}[0-9a-f]{12}$', error="Malformed UUID"))

l_id_required = fields.Str(required=True, validate=validate.Regexp('^[0-9a-f]{8}[0-9a-f]{4}[0-5][0-9a-f]{3}[089ab][0-9a-f]{3}[0-9a-f]{12}$', error="Malformed UUID"))
l_id = fields.Str(validate=validate.Regexp('^[0-9a-f]{8}[0-9a-f]{4}[0-5][0-9a-f]{3}[089ab][0-9a-f]{3}[0-9a-f]{12}$', error="Malformed UUID"))

string_required = fields.Str(validate=validate.Length(min=1, max=256), required=True)
string = fields.Str(validate=validate.Length(min=1, max=256))

statuses = ["Operational", "Maintenance", "Decommissioned"]
status_required = fields.Str(required=True, validate=validate.OneOf(statuses))
status = fields.Str(validate=validate.OneOf(statuses))

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planet_required = fields.Str(required=True, validate=validate.OneOf(planets))
planet = fields.Str(validate=validate.OneOf(planets))

capacity_required = fields.Integer(required=True, validate=validate.Range(min=1, error="Value must be greater than 0"))
capacity = fields.Integer(validate=validate.Range(min=1, error="Value must be greater than 0"))

class SIDSchema(Schema):
    s_id = s_id_required

    class Meta:
        # If there are extra fields then ignore them. Allows for the extraction of 
        # specific starship data
        unknown = EXCLUDE
    
    @post_load
    def get_spaceship(self, data, **kwargs):
        if not data['s_id'] in spaceships:
            abort(400, "Invalid s_id: Spaceship does not exist")
        return spaceships[data['s_id']]

class LIDSchema(Schema):
    l_id = l_id_required

    class Meta:
        unknown = EXCLUDE

    @post_load
    def get_location(self, data, **kwargs):
        if not data['l_id'] in locations:
            abort(400, "Invalid l_id: Location does not exist")
        return locations[data['l_id']]

class LocationPostSchema(Schema):
    name = string_required
    planet = planet_required
    capacity = capacity_required

    @post_load
    def make_location(self, data, **kwargs):
        data['id'] = uuid.uuid4().hex
        return Location(**data)

class LocationUpdateSchema(Schema):
    name = string
    planet = planet
    capacity = capacity

class SpaceshipPostSchema(Schema):
    name = string_required
    model = string_required
    l_id = l_id_required
    status = status_required

    @post_load
    def make_spaceship(self, data, **kwargs):
        if not data['l_id'] in locations:
            abort(400, "Invalid l_id: Location does not exist")
        data['id'] = uuid.uuid4().hex
        return Spaceship(**data)

class SpaceshipUpdateSchema(Schema):
    name = string
    model = string
    status = status

    class Meta():
        unknown = EXCLUDE