from __future__ import annotations
import pygame

from beelisete.src.views.menu import Menu
from beelisete.src.views.sceneManager import SceneManager

class Application:

    def __init__(self):
        self.screen = pygame.display.set_mode((1080, 720))
        self.scene_manager = SceneManager()
        self.scene_manager.go_to(Menu())
        self.is_running = True

    def run(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

                self.scene_manager.current_scene.handle_event(event)
            
            self.scene_manager.current_scene.update()
            self.scene_manager.current_scene.render(self.screen)
            pygame.display.flip()
