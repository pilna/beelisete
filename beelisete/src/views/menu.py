import pygame
from random import choices, randint

from beelisete.src.views.scene import Scene
from beelisete.src.views.game import Game
from beelisete.src.views.option import Option
from beelisete.src.views.Button import Button
from beelisete.src.model.tile import Tile
from beelisete.src.model.bigDemon import BigDemon
from beelisete.src.model.player import Player
from beelisete.src.model.lizard import Lizard

class Menu(Scene):

    def __init__(self):
        Scene.__init__(self)
        self.buttons = [
            Button("Play", 0, 80, 1080, 150, on_click=self.go_to_game_scene),
            Button("Options", 0, 280, 1080, 150, on_click=self.go_to_options_scene),
            Button("Quit", 0, 480, 1080, 150, on_click=self.close_application)
        ]
        self.index_active_button = 0
        self.backgrounds = self.__load_background()
        self.walls = self.__load_walls()
        self.entities = self.generate_entities()
        self.__load_music()
    

    def generate_entities(self):
        entities = []

        for _ in range(randint(2, 5)):
            x, y = randint(32, 1048), randint(64, 688)
            entities.append(BigDemon(x, y))
        
        for _ in range(randint(2, 5)):
            x, y = randint(32, 1048), randint(64, 688)
            entities.append(Lizard(x, y))

        entities.append(Player(randint(32, 1048), randint(64, 688)))

        return entities
        
    
    def __load_music(self):
        pygame.mixer.music.unload()
        pygame.mixer.music.load("beelisete/assets/sounds/01_Invitation.ogg")
        pygame.mixer.music.play(-1)


    def __load_background(self):
        backgrounds = []

        for y in range(0, 720, 32):
            for x in range(0, 1080, 32):
                floor_type = choices(["grass", "flower"], weights=[70, 30])[0]
                floor_name = f"{floor_type}_{randint(1, 16)}"
                backgrounds.append(Tile(floor_name, x, y))
        
        return backgrounds


    def __load_walls(self):
        walls = [
            Tile("wall_corner_left", 0, 0),
            Tile("wall_corner_right", 1048, 0),
            Tile("border_lower_left", 0, 688),
            Tile("border_lower_right", 1048, 688)
        ]

        for x in range(32, 1048, 64):
            walls.append(Tile("small_front_wall_2", x, 0))
            walls.append(Tile("horizontal_bot_border", x, 688))
            walls.append(Tile("horizontal_bot_border", x + 32, 688))

        for y in range(64, 688, 32):
            walls.append(Tile("vertical_border_left", 0, y))
            walls.append(Tile("vertical_border_right", 1048, y))

        return walls

    def close_application(self):
        pygame.quit()
        exit()
    

    def go_to_options_scene(self):
        self.scene_manager.go_to(Option())


    def go_to_game_scene(self):
        self.scene_manager.go_to(Game())
        

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

            button.text_color = (255, 255, 255) if i == self.index_active_button else (0, 0, 0)


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
        
