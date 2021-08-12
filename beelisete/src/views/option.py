import pygame

from beelisete.src.views.scene import Scene
from beelisete.src.views.Button import Button

class Option(Scene):

    def __init__(self):
        Scene.__init__(self)
        self.buttons = [
            
        ]
    
    def handle_event(self, event: pygame.event.Event) -> None:
        pass
    
    def update(self) -> None:
        pass

    def render(self, surface: pygame.Surface) -> None:
        surface.fill((0, 200, 100))
