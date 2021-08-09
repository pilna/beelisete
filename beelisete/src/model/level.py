


class Level:

    def __init__(self, rooms, spawn_room, exit_room):
        self.rooms = rooms
        self.spawn_room = spawn_room
        self.exit_room = exit_room
    
    @classmethod
    def generate(cls, width, height):
        pass