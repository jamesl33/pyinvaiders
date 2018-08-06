#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""


import pygame

from constants import TANK_EXPLOSION
from explosion import Explosion
from sprite_sheet import SpriteSheet


class TankExplosion(Explosion):
    """The sprite which represents the exploding tank.

    Arguments:
        tank (Tank): The tank which is going to explode.
        groups (pygame.sprite.Group): All the groups this sprite will be in.
    """
    animation_speed = 0.5
    images = SpriteSheet.load_sprite_strip(TANK_EXPLOSION, 1)

    def __init__(self, tank, *groups):
        super().__init__(self.images, *groups)
        self.rect.x, self.rect.y = tank.rect.x - 4, tank.rect.y
