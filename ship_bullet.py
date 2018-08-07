#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

import pygame

from bullet import Bullet
from constants import SHIP_BULLET
from sprite_sheet import SpriteSheet


class ShipBullet(Bullet):
    """Bullet which is fired by an alien ship.

    Arguments:
        ship (Ship): The ship which fired the bullet.
        groups (pygame.sprite.Group): The groups the bullet will be added to.

    Attributes:
        image (pygame.Surface): The image representing the sprite.
        dirty (int): Whether or not to redraw the sprite.
        velocity (pygame.math.Vector2): The sprites x, y velocities.
    """
    image = SpriteSheet().load_sprite(SHIP_BULLET)

    def __init__(self, ship, *groups):
        super().__init__(self.image, *groups)
        self.dirty = 2
        self.velocity = pygame.math.Vector2(0, -750)

        self.rect.x = ship.rect.x + ship.rect.width / 2 - self.rect.width / 2
        self.rect.y = ship.rect.y + self.rect.height * 2
