#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

from copy import copy

import pygame

from bullet import Bullet
from constants import TANK_BULLET, TANK_BULLET_EXPLOSION
from explosion import Explosion


class TankBullet(Bullet):
    """Bullets which are fired by the user controlled tank.

    Arguments:
        tank (Tank): The tank which fired the bullet.
        groups (pygame.sprite.Group): All the groups this entity will be in.

    Attributes:
        image (pygame.Surface): The current image which represents the sprite.
        rect (pygame.Rect): The rect used for placing the sprite.
        mask (pygame.mask.Mask): The mast for the image.
        _explosion (Animation): The explosion animation.
        _velocity (pygame.math.Vector2): The x, y velocities for the sprite.
    """
    def __init__(self, tank, *groups):
        super().__init__(*groups)
        self.image = copy(tank.bullet).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self._explosion = copy(tank.bullet_explosion)
        self._velocity = pygame.math.Vector2(0, -750)

        self.rect.x = tank.rect.x + tank.rect.width / 2 - TANK_BULLET.width / 2
        self.rect.y = tank.rect.y - TANK_BULLET.height

    def take_damage(self, bullets, *groups):
        """Take any damage from other bullets and make sure that the bullet is
        destroyed when it is no longer on the display.

        Arguments:
            bullets (pygame.sprite.Group): The group of bullets.
            groups (pygame.sprite.Group): The groups the explosion will be in.
        """
        super().take_damage(bullets, *groups)

        if self.rect.y <= 0:
            self.kill()
            Explosion(self._explosion,
                      (self.rect.x - TANK_BULLET_EXPLOSION.width / 2, 0),
                      *groups)
