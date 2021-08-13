from abc import ABC, abstractmethod

import beelisete.src.config as cfg

class Camera:

    def __init__(self, entity):
        self.entity = entity
        self.offset_x = 0
        self.offset_y = 0
        self.movement = FollowEntity(self)
    
    def update(self):
        self.movement.apply()

    def get_offset(self):
        return self.offset_x, self.offset_y


class CameraMovement(ABC):

    def __init__(self, camera):
        self.camera = camera
        self.entity = camera.entity
    
    @abstractmethod
    def apply(self):
        raise NotImplementedError()


class FollowEntity(CameraMovement):

    def __init__(self, camera):
        super().__init__(camera)
        self.center_x = cfg.WIDTH // 2 - self.entity.width // 2
        self.center_y = cfg.HEIGHT // 2 - self.entity.height // 2
    
    def apply(self):
        self.camera.offset_x = self.entity.x - self.center_x
        self.camera.offset_y = self.entity.y - self.center_y