import pygame

from beelisete.src.views.scene import Scene
from beelisete.src.model.level import Level


class Game(Scene):

    def __init__(self):
        Scene.__init__(self)
        self.player = None
        self.level = Level.generate(5, 5)
        # self.current_room = self.level.spawn_room
        self.__load_music()
    
    def __load_music(self):
        pygame.mixer.music.unload()
        pygame.mixer.music.load("beelisete/assets/sounds/04_Hopeful_Feeling.ogg")
        pygame.mixer.music.play(-1)
    
    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self) -> None:
        pass
    
    def render(self, surface: pygame.Surface) -> None:
        surface.fill((200, 140, 170))