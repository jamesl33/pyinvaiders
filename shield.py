#!/usr/bin/env python3
"""
This file is part of pyinvaiders.

Copyright (C) 2019, James Lee <jamesl33info@gmail.com>.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from copy import copy
from random import randint

import pygame

from constants import SHIELD
from entity import Entity
from sprite_sheet import SpriteSheet


class Shield(Entity):
    """Shield which is placed between the user and the alien horde.

    Arguments:
        position (tuple {int, int}): The position to place the shield.
        groups (pygame.sprite.Group): All the groups this entity will be in.

    Attributes:
        image (pygame.Surface): The current image which represents the sprite.
        rect (pygame.Rect): The rect used for placing the sprite.
        mask (pygame.mask.Mask): The mast for the image.
    """
    shield = SpriteSheet.sprite(SHIELD)

    def __init__(self, position, *groups):
        super().__init__(*groups)
        self.image = copy(self.shield).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.topleft = position

    def take_damage(self, bullets):
        """Take damage from the bullets on the display.

        Arguments:
            bullets (pygame.sprite.Group): The groups which contains bullets.
        """
        for bullet in bullets:
            try:
                pos_x, pos_y = pygame.sprite.collide_mask(self, bullet)
                bullet.kill()
                self.dirty = 1
            except TypeError:
                continue

            destroy_rect = pygame.Rect((pos_x - 4, pos_y, 8, 8))
            self.image.fill((0, 0, 0, 0), destroy_rect)

            for _ in range(10):
                destroy_x = randint(pos_x - 4, pos_x + 4)
                destroy_y = randint(pos_y - 4, pos_y + 4)
                destroy_rect = (destroy_x - 2, destroy_y, 4, 4)
                self.image.fill((0, 0, 0, 0), destroy_rect)

            for _ in range(20):
                destroy_x = randint(pos_x - 8, pos_x + 8)
                destroy_y = randint(pos_y - 8, pos_y + 8)
                destroy_rect = (destroy_x - 1, destroy_y, 2, 2)
                self.image.fill((0, 0, 0, 0), destroy_rect)

            for _ in range(30):
                destroy_x = randint(pos_x - 12, pos_x + 12)
                destroy_y = randint(pos_y - 12, pos_y + 12)
                destroy_rect = pygame.Rect((destroy_x - 0.5, destroy_y, 1, 1))
                self.image.fill((0, 0, 0, 0), destroy_rect)

            self.mask = pygame.mask.from_surface(self.image)
