from os import listdir, path
import pygame


def is_png(file_name):
    return file_name.split(".")[-1] == "png" if "." in file_name else False


def get_img_from_file(path_directory):
    return [
        pygame.image.load(path.join(path_directory, img_name))
        for img_name in listdir(path.join(path_directory))
        if is_png(img_name)
    ]


def load_animations(image_path):
    animations_img = {}

    for file_name in listdir(image_path):
        current_path = path.join(image_path, file_name)
        if path.isdir(current_path):
            animations_img[file_name] = get_img_from_file(current_path)
    
    return animations_img


def Animated(image_path, animation_speed=0.2):
    def Decorate(cls):
        constructor = cls.__init__

        def __init__(self, *args, **kwargs):
            self.image_path = image_path
            self.current_animation = "default"
            self.animation_index = 0
            self.animation_speed = animation_speed
            constructor(self, *args, **kwargs)
        
        def set_animation(self, animation_name):
            self.current_animation = animation_name
            self.animation_index = 0

        def get_image(self):
            self.animation_index += self.animation_speed
            return type(self).ANIMATIONS[self.current_animation][int(self.animation_index) % len(type(self).ANIMATIONS[self.current_animation])]
        
        cls.ANIMATIONS = load_animations(image_path)
        cls.__init__ = __init__
        cls.get_image = get_image
        cls.set_animation = set_animation
        return cls
    return Decorate

