from flask import abort

spaceships = {}
locations = {}

def add_location(location):
    locations[location.id] = location

def add_spaceship(spaceship):
    spaceships[spaceship.id] = spaceship

class Spaceship():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.json = kwargs
        self.location = locations[self.l_id]
        if self.location.is_full():
            abort(400, "Location is at capacity")
        self.location.add_spaceship(self)

    def get_json(self):
        return {"name": self.name, "id": self.id, "model": self.model, "status": self.status, "l_id": self.l_id}

class Location():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.json = kwargs
        self.s_ids = []
        self.spaceships = []
        self.num_spaceships = 0

    def is_full(self):
        return self.num_spaceships >= self.capacity

    def add_spaceship(self, spaceship):
        self.num_spaceships += 1
        self.s_ids.append(spaceship.id)
        self.spaceships.append(spaceship)

    def get_json(self):
        return {"name": self.name, "id": self.id, "planet": self.planet, "capacity": self.capacity, "num_spaceships": self.num_spaceships, "s_ids": self.s_ids}