import pygame

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
    

    def get_rectangle(self):
        return pygame.Rect(self.x, self.y, Tile.image[self.name].get_width(), Tile.image[self.name].get_height())
    

    def display(self, surface, offset=(0, 0)):
        surface.blit(type(self).image[self.name], (self.x - offset[0], self.y - offset[1]))
    