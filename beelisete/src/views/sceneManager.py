

class SceneManager:

    def __init__(self, starting_scene):
        self.current_scene = starting_scene
    
    def go_to(self, scene):
        self.current_scene = scene