#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""


from constants import SHIP_TYPE_ONE
from ship import Ship
from sprite_sheet import SpriteSheet


class ShipTypeOne(Ship):
    """The first type of alien ship.

    Arguments:
        position (tuple {int, int}): The positon to place the ship.
        groups (pygame.sprite.Group): All the groups this sprite will be in.

    Attributes:
        image (pygame.Surface): The image representing the sprite.
    """
    image = SpriteSheet.load_sprite(SHIP_TYPE_ONE)

    def __init__(self, position, *groups):
        super().__init__(self.image, *groups)

        self.rect.x, self.rect.y = position
