import pygame

from beelisete.src.views.scene import Scene
from beelisete.src.views.Button import Button
from beelisete.src.model.tile import Tile

class Menu(Scene):

    def __init__(self):
        self.buttons = [Button("start", 100, 100, 300, 150, (200, 100, 60))]
        self.tiles = [Tile("wall_corner_left", 0, 0), Tile("wall_front", 32, 0)]

    def handle_event(self, event: pygame.event.Event):
        for button in self.buttons:
            if button.mouse_is_over(pygame.mouse.get_pos()):
                button.color = (244, 20, 50)
    
    def update(self):
        pass

    def render(self, surface: pygame.Surface):
        for button in self.buttons:
            button.display(surface)
        
        for tile in self.tiles[::-1]:
            tile.display(surface)