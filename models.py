from flask import abort
from pprint import pprint

# data stores
spaceships = {}
locations = {}

# Static helper functions

def add_location(location):
    locations[location.id] = location

def add_spaceship(spaceship):
    spaceships[spaceship.id] = spaceship

def get_s_ids():
    s_ids = []
    for s_id in spaceships:
        s_ids.append(s_id)
    return s_ids

def get_l_ids():
    l_ids = []
    for l_id in locations:
        l_ids.append(l_id)
    return l_ids

# Models

class Spaceship():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.json = kwargs
        self.location = locations[self.l_id]
        if self.location.is_full():
            abort(400, "Location is at capacity")
        self.location.add_spaceship(self)

    def delete(self):
        del spaceships[self.id]
        self.location.remove_spaceship(self)

    def travel(self, location):
        if location.is_full():
            abort(400, "Location is at capacity")
        
        if not self.status == "Operational":
            abort(400, "Spaceship is inoperable")

        # Remove self from previous location, update self and new location 
        self.location.remove_spaceship(self)
        self.location = location
        self.location.add_spaceship(self)
        self.l_id = self.location.id

    def update(self, update_dict):
        self.__dict__.update(update_dict)

    def get_json(self):
        return {"name": self.name, "id": self.id, "model": self.model, "status": self.status, "l_id": self.l_id}

class Location():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.json = kwargs
        self.s_ids = []
        self.spaceships = []
        self.num_spaceships = 0

    def delete(self):
        for spaceship in self.spaceships:
            spaceship.delete()
        del locations[self.id]

    def remove_spaceship(self, spaceship):
        self.spaceships.remove(spaceship)
        self.s_ids.remove(spaceship.id)
        self.num_spaceships -= 1

    def is_full(self):
        return self.num_spaceships >= self.capacity

    def add_spaceship(self, spaceship):
        self.num_spaceships += 1
        self.s_ids.append(spaceship.id)
        self.spaceships.append(spaceship)

    def get_json(self):
        return {"name": self.name, "id": self.id, "planet": self.planet, "capacity": self.capacity, "num_spaceships": self.num_spaceships, "s_ids": self.s_ids}