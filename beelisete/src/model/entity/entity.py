from abc import ABCMeta, abstractmethod
import pygame

class Entity(metaclass=ABCMeta):

    def __init__(self, x, y, width, height, heal_point, max_heal=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
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
    
    def display(self, surface, offset=(0, 0)):
        surface.blit(pygame.transform.scale(self.get_image(), (self.width, self.height)), (self.x - offset[0], self.y - offset[1]))