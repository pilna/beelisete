from beelisete.src.model.camera import Camera
import pygame

import beelisete.src.config as cfg
from beelisete.src.model.color import Color
from beelisete.src.model.camera import Camera
from beelisete.src.views.scene import Scene
from beelisete.src.model.tile import Tile
from beelisete.src.model.entity.player import Player

class RoomEditor(Scene):

    def __init__(self) -> None:
        Scene.__init__(self)
        self.player = Player(0, 0)
        self.camera = Camera(self.player)
        self.tiles = [
            Tile("flower_6", 0, 0),
            Tile("flower_3", -64, -64),
            Tile("grass_1", -946, -512)
        ]
        self.show_grid = True


    def display_grid(self, surface):
        # TODO find mathematical correlation and remoove magic value
        offset_x, offset_y = self.camera.get_offset()
        entity_x, entity_y = self.camera.entity.x, self.camera.entity.y
        
        for y in range((entity_y // cfg.TILE_HEIGHT) * cfg.TILE_HEIGHT, cfg.HEIGHT + entity_y, cfg.TILE_HEIGHT):
            start_point = offset_x, y - entity_y
            arrival_point = cfg.WIDTH, y - entity_y
            pygame.draw.line(surface, Color.black, start_point, arrival_point)
        
        for x in range((entity_x // cfg.TILE_WIDTH) * cfg.TILE_WIDTH, cfg.WIDTH + entity_x, cfg.TILE_WIDTH):
            start_point = x + 16 - entity_x, 0
            arrival_point = x + 16 - entity_x, cfg.HEIGHT
            pygame.draw.line(surface, Color.black, start_point, arrival_point)
    
    
    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_z, pygame.K_s]:
                self.player.velocity_y = 0
            if event.key in [pygame.K_q, pygame.K_d]:
                self.player.velocity_x = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                self.player.velocity_y = -1
            if event.key == pygame.K_s:
                self.player.velocity_y = 1
            if event.key == pygame.K_d:
                self.player.velocity_x = 1
            if event.key == pygame.K_q:
                self.player.velocity_x = -1
            if event.key == pygame.K_e:
                self.show_grid = not self.show_grid
            

    def update(self) -> None:
        self.player.update()
        self.camera.update()
    
    def render(self, surface: pygame.Surface) -> None:
        surface.fill(Color.white)

        if self.show_grid:
            self.display_grid(surface)

        for tile in self.tiles:
            tile.display(surface, self.camera.get_offset())
        