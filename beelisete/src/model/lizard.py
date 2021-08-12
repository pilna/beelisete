from beelisete.src.model.Entity import Entity
from beelisete.src.model.animation import Animated

@Animated("beelisete/assets/animations/lizard")
class Lizard(Entity):

    def __init__(self, x, y):
        super().__init__(x, y, 3)