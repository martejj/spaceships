from marshmallow import Schema, fields, ValidationError, validates, validate, EXCLUDE

s_id_required = fields.UUID(required=True)
s_id = fields.UUID()

l_id_required = fields.UUID(required=True)
l_id = fields.UUID()

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

class LIDSchema(Schema):
    l_id = l_id_required

    class Meta:
        unknown = EXCLUDE

class LocationPostSchema(Schema):
    name = string_required
    planet = planet_required
    capacity = capacity_required

class LocationUpdateSchema(Schema):
    name = string
    planet = planet
    capacity = capacity

class SpaceshipPostSchema(Schema):
    name = string_required
    model = string_required
    location = l_id_required
    status = status_required

class SpaceshipUpdateSchema(Schema):
    name = string
    model = string
    location = l_id
    status = status