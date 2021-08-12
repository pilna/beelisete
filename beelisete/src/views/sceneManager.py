import pygame

class SceneManager:

    def __init__(self):
        self.current_scene = None
    
    def go_to(self, scene):
        scene.scene_manager = self
        self.current_scene = scene