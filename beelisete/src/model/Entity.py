from abc import ABCMeta, abstractmethod

class Entity(metaclass=ABCMeta):

    def __init__(self, x, y, heal_point, max_heal=0):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.heal_point = heal_point
        self.max_heal = max(heal_point, max_heal)

    def get_image(self):
        raise NotImplementedError
    
    def take_damage(self, damage_amount):
        self.heal_point = max(self.heal_point - damage_amount, 0)
    
    def heal(self, heal_amount):
        self.heal_point = min(self.heal_point + heal_amount, self.max_heal)
    
    def is_alive(self):
        return self.heal_point > 0
    
    def display(self, surface):
        surface.blit(self.get_image(), (self.x, self.y))