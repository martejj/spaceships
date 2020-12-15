
spaceships = {}
locations = {}

class Spaceship():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.json = kwargs
        self.location = locations[self.l_id]
        spaceships[self.id] = self

    def json(self):
        return self.json

class Location():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.json = kwargs
        locations[self.id] = self

    def json(self):
        return self.json