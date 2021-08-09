from beelisete.src.model.direction import Direction


class Room:

    def __init__(self):
        self.tiles = []
        self.entities = []
        self.collectables = []
        self.neighbores_room = {
            Direction.RIGHT: None,
            Direction.LEFT: None,
            Direction.UP: None,
            Direction.DOWN: None
        }
    
    def render(self, surface):
        for tile in self.tiles:
            tile.display(surface)

        for collectable in self.collectables:
            collectable.display(surface)
        
        for entity in self.entities:
            entity.display(surface)

        