#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

import pygame

from bullet import Bullet
from constants import TANK_BULLET
from sprite_sheet import SpriteSheet
from tank_bullet_explosion import TankBulletExplosion


class TankBullet(Bullet):
    """The bullet which will be fired from the user controlled Tank.

    Arguments:
        tank (Tank): The tank sprite which fired the bullet.
        groups (pygame.sprite.Group): All the groups this sprite will be in.

    Attributes:
        image (pygame.Surface): The image representing the sprite.
        dirty (int): Determine if the sprite should be redrawn or not.
        velocity (pygame.math.Vector2): Movement velocity in the x, y axis.
    """
    image = SpriteSheet().load_sprite(TANK_BULLET)

    def __init__(self, tank, *groups):
        super().__init__(self.image, *groups)
        self.dirty = 2
        self.velocity = pygame.math.Vector2(0, 750)

        self.rect.x = tank.rect.x + tank.rect.width / 2 - self.rect.width / 2
        self.rect.y = tank.rect.y - self.rect.height

    def move(self, *groups):
        if self.rect.y <= 0:
            TankBulletExplosion(self, *groups)
            self.kill()

        super().move()
