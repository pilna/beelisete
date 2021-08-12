from beelisete.src.model.entity.entity import Entity
from beelisete.src.model.animation import Animated


@Animated("beelisete/assets/animations/big_demon", animation_speed=0.1)
class BigDemon(Entity):

    def __init__(self,x, y):
        super().__init__(x, y, 32, 56, 5)