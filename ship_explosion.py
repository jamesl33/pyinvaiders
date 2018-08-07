#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

from constants import SHIP_EXPLOSION
from explosion import Explosion
from sprite_sheet import SpriteSheet


class ShipExplosion(Explosion):
    """The sprite which represents the exploding ship.

    Arguments:
        ship (Ship): The ship which is going to explode.
        groups (pygame.sprite.Group): All the groups this sprite will be in.

    Attributes:
        animation_speed (float): The time to wait before advancing the
            advancing the animation.
        images (list [pygame.Surface]): The animation frames.
    """
    animation_speed = 0.3
    images = SpriteSheet.load_sprite_strip(SHIP_EXPLOSION, 1)

    def __init__(self, ship, *groups):
        super().__init__(self.images, *groups)
        self.rect.x, self.rect.y = ship.rect.x, ship.rect.y
