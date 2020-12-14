from flask import request, abort
from marshmallow import ValidationError
from functools import wraps
from pprint import pprint

def validate_body(schema, name='data'):
    def decorator(func):
        @wraps(func)
        def wrapper_body(*args, **kwargs):
            # Validate data
            try:
                data = schema().load(request.get_json())
            except ValidationError as err:
                abort(400, err.messages)

            validated_data = {
                name: data
            }

            kwargs.update(validated_data)

            return func(*args, **kwargs)
        return wrapper_body
    return decorator

def validate_args(schema, name='args_data'):
    def decorator(func):
        @wraps(func)
        def wrapper_args(*args, **kwargs):
            # Validate data
            try:
                data = schema().load(request.args)
            except ValidationError as err:
                abort(400, err.messages)
           
            validated_data = {
                name: data
            }

            kwargs.update(validated_data)

            return func(*args, **kwargs)
        return wrapper_args
    return decorator