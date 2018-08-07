#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

import pygame

from constants import DISPLAY
from sprite import Sprite


class Bullet(Sprite):
    """A base class for any type of bullet.

    Arguments:
        image (pygame.Surface): The image that represents the sprite.
        position (tuple {int, int}): The x, y position to place the sprite.
        velocity (pygame.math.Vector2): The x, y velocity of the sprite.
        groups (pygame.sprite.Group): All the groups this sprite will be in.

    Attributes:
        dirty (int): Whether or not too redraw the sprite.
        image (pygame.Surface): The image which represents the bullet.
        mask (pygame.Mask): The image's mask.
        rect (pygame.Rect): The image's rect.
        velocity (pygame.math.Vector2): The x, y velocity of the sprite.
    """
    def __init__(self, image, position, velocity, *groups):
        super().__init__(*groups)
        self.dirty = 2
        self.image = image.convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.velocity = velocity

        self.rect.x, self.rect.y = position

    def move(self):
        """Update the bullets position depending on the objects time based
        variables."""
        self.rect.y -= int(self.seconds_elapsed * self.velocity.y)

        if not self.rect.colliderect(DISPLAY):
            self.kill()

    def take_damage(self, bullets):
        """See if any of the bullets have come in contact with each other."""
        for bullet in bullets:
            if bullet is self:
                continue

            if pygame.sprite.collide_rect(self, bullet):
                # TODO - Create a bullet explosion sprite.
                bullet.kill()
                self.kill()
