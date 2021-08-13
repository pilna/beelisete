import pygame
from random import choices, randint

import beelisete.src.config as cfg
from beelisete.src.views.scene import Scene
from beelisete.src.views.game import Game
from beelisete.src.views.option import Option
from beelisete.src.views.roomEditor import RoomEditor
from beelisete.src.model.button import Button
from beelisete.src.model.tile import Tile
from beelisete.src.model.entity.bigDemon import BigDemon
from beelisete.src.model.entity.player import Player
from beelisete.src.model.entity.lizard import Lizard
from beelisete.src.model.color import Color

class Menu(Scene):

    def __init__(self):
        Scene.__init__(self)
        self.buttons = [
            Button("Play", 0, 0, cfg.WIDTH, 150, on_click=self.go_to_game_scene),
            Button("Room Editor", 0, 0, cfg.WIDTH, 150, on_click=self.go_to_room_editor),
            Button("Options", 0, 0, cfg.WIDTH, 150, on_click=self.go_to_options_scene),
            Button("Quit", 0, 0, cfg.WIDTH, 150, on_click=self.close_application)
        ]
        self.index_active_button = 0
        self.backgrounds = self.__load_background()
        self.walls = self.__load_walls()
        self.entities = self.__generate_entities()
        self.__load_music()
        self.__set_y_button()

    def __set_y_button(self):
        height_all_button = sum(button.height for button in self.buttons)
        space_y_between_button = (cfg.HEIGHT - height_all_button) // (len(self.buttons) + 1)

        if self.buttons:
            self.buttons[0].y = space_y_between_button

        for i in range(1, len(self.buttons)):
            previous_button, current_button = self.buttons[i - 1], self.buttons[i]
            current_button.y = previous_button.y + previous_button.height + space_y_between_button
    

    def __generate_entities(self):
        entities = []

        spawn_x_min, spawn_x_max = cfg.TILE_WIDTH, cfg.WIDTH - cfg.TILE_WIDTH
        spawn_y_min, spawn_y_max = cfg.TILE_HEIGHT * 2, cfg.HEIGHT - cfg.TILE_HEIGHT

        for _ in range(randint(2, 5)):
            x, y = randint(spawn_x_min, spawn_x_max), randint(spawn_y_min, spawn_x_max)
            entities.append(BigDemon(x, y))
        
        for _ in range(randint(2, 5)):
            x, y = randint(spawn_x_min, spawn_x_max), randint(spawn_y_min, spawn_y_max)
            entities.append(Lizard(x, y))

        entities.append(Player(randint(spawn_x_min, spawn_x_max), randint(spawn_y_min, spawn_y_max)))

        return entities
        
    
    def __load_music(self):
        pygame.mixer.music.unload()
        pygame.mixer.music.load("beelisete/assets/sounds/01_Invitation.ogg")
        pygame.mixer.music.play(-1)


    def __load_background(self):
        backgrounds = []

        for y in range(0, cfg.HEIGHT, cfg.TILE_HEIGHT):
            for x in range(0, cfg.WIDTH, cfg.TILE_WIDTH):
                floor_type = choices(["grass", "flower"], weights=[70, 30])[0]
                floor_name = f"{floor_type}_{randint(1, 16)}"
                backgrounds.append(Tile(floor_name, x, y))
        
        return backgrounds


    def __load_walls(self):
        walls = [
            Tile("wall_corner_left", 0, 0),
            Tile("wall_corner_right", cfg.WIDTH - cfg.TILE_WIDTH, 0),
            Tile("border_lower_left", 0, cfg.HEIGHT - cfg.TILE_HEIGHT),
            Tile("border_lower_right", cfg.WIDTH - cfg.TILE_WIDTH, cfg.HEIGHT - cfg.TILE_HEIGHT)
        ]

        for x in range(cfg.TILE_WIDTH, cfg.WIDTH - cfg.TILE_WIDTH, cfg.TILE_WIDTH * 2):
            walls.append(Tile("small_front_wall_2", x, 0))
            walls.append(Tile("horizontal_bot_border", x, cfg.HEIGHT - cfg.TILE_HEIGHT))
            walls.append(Tile("horizontal_bot_border", x + cfg.TILE_WIDTH, cfg.HEIGHT - cfg.TILE_HEIGHT))

        for y in range(cfg.TILE_HEIGHT * 2, cfg.HEIGHT - cfg.TILE_HEIGHT, cfg.TILE_HEIGHT):
            walls.append(Tile("vertical_border_left", 0, y))
            walls.append(Tile("vertical_border_right", cfg.WIDTH - cfg.TILE_WIDTH, y))

        return walls

    def close_application(self):
        pygame.quit()
        exit()
    

    def go_to_options_scene(self):
        self.scene_manager.go_to(Option())


    def go_to_game_scene(self):
        self.scene_manager.go_to(Game())
    
    
    def go_to_room_editor(self):
        self.scene_manager.go_to(RoomEditor())
        

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.buttons[self.index_active_button].on_click()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.index_active_button = (self.index_active_button + 1) % len(self.buttons)
            if event.key == pygame.K_UP:
                self.index_active_button = (self.index_active_button - 1) % len(self.buttons)
            if event.key == pygame.K_RETURN:
                self.buttons[self.index_active_button].on_click()

    
    def update(self):
        for i, button in enumerate(self.buttons):
            if button.mouse_is_over(pygame.mouse.get_pos()):
                self.index_active_button = i

            button.text_color = Color.white if i == self.index_active_button else Color.black


    def render(self, surface: pygame.Surface):
        surface.fill((30, 30, 30))
        
        for tile in self.backgrounds:
            tile.display(surface)
        
        for tile in self.walls:
            tile.display(surface)

        for entity in self.entities:
            entity.display(surface)
        
        for button in self.buttons:
            button.display(surface)
        
