import pygame

class Button:

    def __init__(self, text, x, y, width, height, color, on_click=None) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.on_click = on_click
        self.font = pygame.font.SysFont('comicsans', 60)
        self.text = self.font.render(text, 1, (0, 0, 0))
    
    def mouse_is_over(self, mouse_position):
        mouse_x, mouse_y = mouse_position
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height
    
    def display(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        surface.blit(self.text, (self.x + (self.width // 2 - self.text.get_width() // 2), self.y + (self.height // 2 - self.text.get_height() // 2)))


