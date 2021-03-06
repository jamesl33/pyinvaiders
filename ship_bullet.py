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

from constants import DISPLAY, SHIP_BULLET_VECOLCITY, SHIP_BULLET_EXPLOSION
from bullet import Bullet
from explosion import Explosion


class ShipBullet(Bullet):
    """A bullet which will be fired by any of the ships.

    Arguments:
        ship (Ship): The ship that fired the bullet.
        groups (pygame.sprite.Group): The groups the sprite will be in.

    Attributes:
        _bullet_type (int): The type of bullet this is.
        _animation (Animation): The bullets animation looping animation.
        _explosion (Animation): The bullets explosion animation.
        image (pygame.Surface): The image which represents the sprite.
        rect (pygame.Rect): The rect used to place the sprite.
        mask (pygame.mask.Mask): The mask used for collision detection.
        _velocity (pygame.math.Vector2): The x, y velocities for the sprite.
        _last_frame (float): The last animation frame which was drawn.
    """
    def __init__(self, ship, *groups):
        super().__init__(*groups)
        self._bullet_type = ship.type

        if self.type == 1:
            self._animation = copy(ship.type_one['bullet'])
            self._explosion = copy(ship.type_one['bullet_explosion'])
        elif self.type == 2:
            self._animation = copy(ship.type_two['bullet'])
            self._explosion = copy(ship.type_two['bullet_explosion'])
        elif self.type == 3:
            self._animation = copy(ship.type_three['bullet'])
            self._explosion = copy(ship.type_three['bullet_explosion'])

        self.image = self._animation.next().convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self._velocity = SHIP_BULLET_VECOLCITY
        self._last_frame = 0

        self.rect.x = ship.rect.x + ship.rect.width / 2 - self.rect.width / 2
        self.rect.y = ship.rect.y + ship.rect.height

    @property
    def type(self):
        """Get the type of bullet this is. This directly corrisponds to type
        of ship which fired the bullet."""
        return self._bullet_type

    def update(self, seconds_elapsed):
        """Update the sprites animation depending if the time is correct.

        Arguments:
            seconds_elapsed (float): The time since the last frame was drawn.
        """
        super().update(seconds_elapsed)

        if abs(self._last_frame - self._current_time) >= self._animation.delay:
            self.image = self._animation.next().convert_alpha()
            self._last_frame = self._current_time

    def take_damage(self, bullets, *groups):
        """Take any damage from other bullets and make sure that the bullet is
        destroyed when it is no longer on the display.

        Arguments:
            bullets (pygame.sprite.Group): The group of bullets.
            groups (pygame.sprite.Group): The groups the explosion will be in.
        """
        super().take_damage(bullets, *groups)

        if self.rect.y >= DISPLAY.height:
            self.kill()
            Explosion(self._explosion,
                      (self.rect.x - SHIP_BULLET_EXPLOSION.width / 2,
                       DISPLAY.height - SHIP_BULLET_EXPLOSION.height),
                      *groups)
