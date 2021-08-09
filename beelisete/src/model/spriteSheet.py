import json
import pygame

class SpriteSheet:

    def __init__(self, file_path):
        self.sheet = pygame.image.load(file_path)
    
    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        print(rect)
        image = pygame.Surface(rect.size)
        image.blit(self.sheet, (0, 0), rect)
        return image
    
    @staticmethod
    def load_sprites(url_sprites_list):
        image = {}

        for url in url_sprites_list:
            with open(url) as json_file:
                json_data = json.load(json_file)
                sprite_sheet = SpriteSheet(json_data["spriteSheetURL"])

                for sprite in json_data["sprites"]:
                    image[sprite["name"]] = sprite_sheet.image_at((
                        int(sprite["x"]),
                        int(sprite["y"]),
                        int(sprite["width"]),
                        int(sprite["height"])
                    ))
        
        return image
