#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

import pygame

from constants import DISPLAY, TANK_BULLET
from sprite_sheet import SpriteSheet


class TankBullet(pygame.sprite.DirtySprite):
    """

    Arguments:
        tank (Tank): The tank which fired the bullet.
        groups (pygame.Group): The groups this sprite will be added too.

    Attributes:
        current_time (float): Time since last operation took place.
        dirty (int): Determine if the sprite should be redrawn or not.
        image (pygame.Surface): The image which will represent the sprite.
        rect (pygame.Rect): The rect for 'image'.
        seconds_elapsed (float): Seconds since the last frame was drawn.
        velocity (pygame.Vector2): Movement velocities.
    """
    image = SpriteSheet().load_sprite(TANK_BULLET)

    def __init__(self, tank, *groups):
        super().__init__(*groups)
        self.current_time = 0
        self.dirty = 2
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.seconds_elapsed = 0
        self.velocity = pygame.math.Vector2(0, 750)

        self.rect.x = tank.rect.x + tank.rect.width / 2 - self.rect.width / 2
        self.rect.y = tank.rect.y - self.rect.height

    def update(self, seconds_elapsed):
        """Update bullets time based variables and move the bullet.

        Arguments:
            seconds_elapsed (float): Seconds since the last frame was drawn.
        """
        self.current_time += seconds_elapsed
        self.seconds_elapsed = seconds_elapsed

        self.rect.y -= int(self.seconds_elapsed * self.velocity.y)

        if not self.rect.colliderect(DISPLAY):
            self.kill()
