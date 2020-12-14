#!/bin/sh

export FLASK_APP=run.py
export FLASK_DEBUG=1
pipenv run python3 -m flask run