#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

import random
import pygame

from constants import SHIELD
from sprite_sheet import SpriteSheet


class Shield(pygame.sprite.DirtySprite):
    """A shield that the user can hide behind to avoid bullets from the aliens.

    Arguments:
        position (tuple (int, int)): The position to place the shield.
        groups (pygame.Group): The groups this sprite will be added too.

    Attributes:
        dirty (int): Determine if the sprite should be redrawn or not.
        image (pygame.Surface): The image which will represent the sprite.
        rect (pygame.Rect): The rect for 'image'.
    """
    image = SpriteSheet.load_sprite(SHIELD)

    def __init__(self, position, *groups):
        super().__init__(*groups)
        self.dirty = 1
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.x, self.rect.y = position

    def take_damage(self, bullets):
        """Check if there are any bullets colliding with the shield. If there
        is take some damage and remove the bullet.

        Arguments:
            bullets (pygame.sprite.LayeredDirty): All the bullet sprites.
        """
        for bullet in bullets:
            try:
                pos_x, pos_y = pygame.sprite.collide_mask(self, bullet)
                bullet.kill()
                self.dirty = 1
            except TypeError:
                continue

            self.image.fill((0, 0, 0, 0), pygame.Rect(pos_x - 4, pos_y, 8, 8))

            for _ in range(10):
                destroy_x = random.randint(pos_x - 4, pos_x + 4)
                destroy_y = random.randint(pos_y - 4, pos_y + 4)

                self.image.fill((0, 0, 0, 0),
                                pygame.Rect(destroy_x - 2, destroy_y, 4, 4))

            for _ in range(20):
                destroy_x = random.randint(pos_x - 8, pos_x + 8)
                destroy_y = random.randint(pos_y - 8, pos_y + 8)

                self.image.fill((0, 0, 0, 0),
                                pygame.Rect(destroy_x - 1, destroy_y, 2, 2))

            for _ in range(30):
                destroy_x = random.randint(pos_x - 12, pos_x + 12)
                destroy_y = random.randint(pos_y - 12, pos_y + 12)

                self.image.fill((0, 0, 0, 0),
                                pygame.Rect(destroy_x - 0.5, destroy_y, 1, 1))

            self.mask = pygame.mask.from_surface(self.image)
