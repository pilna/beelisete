from beelisete.src.model.entity.entity import Entity
from beelisete.src.model.animation import Animated

@Animated("beelisete/assets/animations/lizard")
class Lizard(Entity):

    def __init__(self, x, y):
        super().__init__(x, y, 32, 56, 3)