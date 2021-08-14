from beelisete.src.model.camera import Camera
import pygame

import beelisete.src.config as cfg
from beelisete.src.model.color import Color
from beelisete.src.model.camera import Camera
from beelisete.src.model.tilePickerMenu import TilePickerMenu
from beelisete.src.model.direction import Direction
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
            Tile("flower_3", -64, -64)
        ]
        self.tile_picker_menu = TilePickerMenu(cfg.WIDTH - 192, 0, 192, cfg.HEIGHT)
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
        mouse_position = pygame.mouse.get_pos()

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

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.tile_picker_menu.mouse_is_over(mouse_position):
                self.tile_picker_menu.handle_click(mouse_position)
            else:
                self.add_tiles(mouse_position)
        
        if event.type == pygame.MOUSEWHEEL and self.tile_picker_menu.mouse_is_over(mouse_position):
            scroll_direction = Direction.UP if event.y > 0 else Direction.DOWN
            self.tile_picker_menu.handle_scroll(scroll_direction)
            

    def convert_position_in_tiles_base(self, position):
        return position[0] // cfg.TILE_WIDTH * cfg.TILE_WIDTH, position[1] // cfg.TILE_HEIGHT * cfg.TILE_HEIGHT


    def add_tiles(self, mouse_position):
        x = mouse_position[0] + self.camera.offset_x
        y = mouse_position[1] + self.camera.offset_y
        x, y = self.convert_position_in_tiles_base((x, y))
        self.tiles.append(Tile(self.tile_picker_menu.current_tiles_selected.name, x, y))


    def update(self) -> None:
        self.player.update() 
        self.camera.update()
    

    def render(self, surface: pygame.Surface) -> None:
        surface.fill(Color.white)

        if self.show_grid:
            self.display_grid(surface)

        for tile in self.tiles:
            tile.display(surface, self.camera.get_offset())

        self.tile_picker_menu.display(surface, self.camera.get_offset())
        