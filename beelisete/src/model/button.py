import pygame

class Button:

    def __init__(self, text, x, y, width, height, text_color=(0, 0, 0),color=None, on_click=lambda *args: None) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.on_click = on_click
        self.text = text
        self.font = pygame.font.Font('beelisete/assets/font/FutureTimeSplitters.otf', 120)
        self.text_color = text_color
    
    def mouse_is_over(self, mouse_position):
        mouse_x, mouse_y = mouse_position
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height
    
    def display(self, surface):
        text = self.font.render(self.text, 1, self.text_color)

        if self.color is not None:
            pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

        surface.blit(text, (self.x + (self.width // 2 - text.get_width() // 2), self.y + (self.height // 2 - text.get_height() // 2)))


