from beelisete.src.model.camera import Camera
import pygame

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
    
    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self) -> None:
        self.camera.update()
    
    def render(self, surface: pygame.Surface) -> None:
        surface.fill(Color.white)

        for tile in self.tiles:
            tile.display(surface, self.camera.get_offset())