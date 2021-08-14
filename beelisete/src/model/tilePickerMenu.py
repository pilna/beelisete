from beelisete.src.model.direction import Direction
import pygame

import beelisete.src.config as cfg
from beelisete.src.model.color import Color
from beelisete.src.model.tile import Tile

class TilePickerMenu:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tiles = self.__load_tiles()
        self.selected_tile = None
        self.offset_y = 0
        self.current_tiles_selected = self.tiles[0]


    def handle_scroll(self, scroll_direction):
        if scroll_direction == Direction.UP:
            self.offset_y += 64
        else:
            self.offset_y -= 64
        
        self.offset_y = max(0, self.offset_y)
    

    def handle_click(self, mouse_position):
        mouse_x, mouse_y = mouse_position[0] - self.x, mouse_position[1] + self.offset_y
        mouse_rectangle = pygame.Rect(mouse_x, mouse_y, 1, 1)
        print(mouse_rectangle)

        for tile in self.tiles:
            if tile.get_rectangle().colliderect(mouse_rectangle):
                self.current_tiles_selected = tile
                print("pass")


    def mouse_is_over(self, mouse_position):
        mouse_x, mouse_y = mouse_position
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height


    def __load_tiles(self):
        return [
            Tile(name, 32, 96 * i + 32)
            for i, (name, image) in enumerate(Tile.image.items())
        ]

    
    def get_surface(self):
        menu_surface = pygame.Surface((self.width, self.height))
        pygame.draw.rect(menu_surface, Color.grey, (0, 0, self.width, self.height))

        for tile in self.tiles:
            tile.display(menu_surface, offset=(0, self.offset_y))

        return menu_surface


    def display(self, surface, offset=(0, 0)):
        surface.blit(self.get_surface(), (self.x, self.y))
    
