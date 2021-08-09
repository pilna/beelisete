from beelisete.src.model.spriteSheet import SpriteSheet

class Tile:
    image = SpriteSheet.load_sprites([
        "beelisete/assets/sprites/tileset_grass.json",
        "beelisete/assets/sprites/tileset_wall.json"
    ])

    def __init__(self, name, x, y, walkable=True):
        self.name = name
        self.x = x
        self.y = y
        self.walkable = walkable
        print(type(self).image)
    

    def display(self, surface):
        surface.blit(type(self).image[self.name], (self.x, self.y))
    