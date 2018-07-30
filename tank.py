#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

import pygame

from constants import DISPLAY
from sprite_sheet import SpriteSheet
from tank_bullet import TankBullet


class Tank(pygame.sprite.DirtySprite):
    """Tank sprite which the user control to destroy the oncoming alien horde.

    Arguments:
        groups (pygame.Group): The groups this sprite will be added too.

    Attributes:
        current_time (float): Time since last operation took place.
        dirty (int): Determine if the sprite should be redrawn or not.
        reload_speed (float): How many seconds to wait before shooting.
        image (pygame.Surface): The image which will represent the sprite.
        rect (pygame.Rect): The rect for 'image'.
        seconds_elapsed (float): Seconds since the last frame was drawn.
        velocity (pygame.Vector2): Movement velocities.
    """
    image = SpriteSheet().load_sprite(pygame.Rect(0, 48, 52, 32))

    def __init__(self, *groups):
        super().__init__(*groups)
        self.current_time = 1
        self.dirty = 1
        self.reload_speed = 0.5
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.seconds_elapsed = 0
        self.velocity = pygame.math.Vector2(250, 0)

        self.rect.x = DISPLAY.width / 2 - self.rect.width / 2
        self.rect.y = (DISPLAY.height - self.rect.height)

    def update(self, seconds_elapsed):
        """Update tanks time based variables.

        Arguments:
            seconds_elapsed (float): Seconds since the last frame was drawn.
        """
        self.current_time += seconds_elapsed
        self.seconds_elapsed = seconds_elapsed

    def move(self, direction):
        """Move the tank depending on the users input.

        Arguments:
            direction (int): left < 0 < right.
        """
        incriment = int(self.seconds_elapsed * self.velocity.x)

        if direction != 0:
            self.dirty = 1
        if direction < 0 and self.rect.left > incriment:
            self.rect.x -= incriment
        elif direction > 0 and self.rect.right < DISPLAY.height - incriment:
            self.rect.x += incriment

    def shoot(self, *groups):
        """Fire a shot from the tank's cannon if it has reload.

        Arguments:
            groups (pygame.Group): The groups this sprite will be added too.
        """
        if self.current_time >= self.reload_speed:
            TankBullet(self, *groups)
            self.current_time = 0
