#!/usr/bin/python3
"""
This file is part of pyinvaiders.

Copyright (C) 2018, James Lee <jamesl33info@gmail.com>.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from copy import copy

import pygame

from animation import Animation
from constants import BULLET_COLLISION
from entity import Entity
from explosion import Explosion
from sprite_sheet import SpriteSheet


class Bullet(Entity):
    """Base bullet class which handles movement and removal of bullets.

    Arguments:
        groups (pygame.sprite.Group): All the groups this entity will be in.

    Attributes:
        dirty (int): Wether or not the sprite should be drawn.
    """
    explosion = Animation(SpriteSheet.animation(BULLET_COLLISION, 1), 0.3)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.dirty = 2
        self._collision = copy(self.explosion)

    def update(self, seconds_elapsed):
        """Update the bullets position on the display."""
        super().update(seconds_elapsed)
        self.rect.y += int(self._seconds_elapsed * self._velocity.y)

    def take_damage(self, bullets, *groups):
        """Check to see if there are any bullets in contact with each other.
        If any are destroy them both and create a collision explosion.

        Arguments:
            bullets (pygame.sprite.Group): The group of bullets.
            groups (pygame.sprite.Group): The groups the explosion will be in.
        """
        for bullet in bullets:
            if bullet is not self and pygame.sprite.collide_mask(self, bullet):
                bullet.kill()
                self.kill()
                Explosion(self._collision,
                          (self.rect.x - BULLET_COLLISION.width / 2,
                           self.rect.y - BULLET_COLLISION.height / 2),
                          *groups)
