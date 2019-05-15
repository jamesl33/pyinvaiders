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

import pygame

from animation import Animation
from constants import DISPLAY, MYSTERY, MYSTERY_EXPLOSION
from entity import Entity
from explosion import Explosion
from sprite_sheet import SpriteSheet


class Mystery(Entity):
    """The mystery ship which flys accross the screen.

    Arguments:
        direction (int): The direction the ship will move across the screen.
        groups (pygame.sprite.Group): All the groups this entity will be in.

    Attributes:
        ship (Ship): The default image for the ship.
        explosion (Animation): The explosion animation.
        dirty (int): Wether or not to draw the entity.
        image (pygame.Surface): The sprites image.
        rect (pygame.Rect): The rect used to place the sprite.
        _explosion (Animation): The explosion animation.
    """
    ship = SpriteSheet.sprite(MYSTERY)
    explosion = Animation(SpriteSheet.animation(MYSTERY_EXPLOSION, 1), 0.3)

    def __init__(self, direction, *groups):
        super().__init__(*groups)
        self.dirty = 2
        self.image = copy(self.ship).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self._explosion = copy(self.explosion)

        self.rect.y = 0 + self.rect.height

        if direction:
            self._velocity = pygame.math.Vector2(250, 0)
            self.rect.x = 0
        else:
            self._velocity = pygame.math.Vector2(-250, 0)
            self.rect.x = DISPLAY.width

    def update(self, seconds_elapsed):
        """Update the entities time based variables and update the sprites
        position.

        Arguments:
            seconds_elapsed (float): The time since the last frame was drawn.
        """
        super().update(seconds_elapsed)
        self.rect.x += int(self._seconds_elapsed * self._velocity.x)

        if not self.rect.colliderect(DISPLAY):
            self.kill()

    def take_damage(self, bullets, *groups):
        """Take any damage from the bullets on the screen. Create an explosion
        animation when the entities died.

        bullets (pygame.sprite.Group): The group containing the bullet sprites.
        groups (pygame.sprite.Group): The groups the explosion will be in.
        """
        for bullet in bullets:
            if pygame.sprite.collide_mask(self, bullet):
                Explosion(self._explosion,
                          (self.rect.x + 6, self.rect.y),
                          *groups)
                bullet.kill()
                self.kill()
