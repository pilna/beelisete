import pygame
from beelisete.src.application import Application

pygame.init()
pygame.mixer.init()
Application().run()
pygame.quit()