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
from constants import (TYPE_ONE, TYPE_ONE_BULLET, TYPE_ONE_EXPLOSION, TYPE_TWO,
                       TYPE_TWO_BULLET, TYPE_TWO_EXPLOSION, TYPE_THREE,
                       TYPE_THREE_BULLET, TYPE_THREE_EXPLOSION,
                       SHIP_BULLET_EXPLOSION)
from entity import Entity
from explosion import Explosion
from sprite_sheet import SpriteSheet
from ship_bullet import ShipBullet


class Ship(Entity):
    """The different types of ships that the user has to fight against.

    Arguments:
        ship_type (int): Which type of ship to create.
        position (tuple {int, int}): The positon to place the ship.
        groups (pygame.sprite.Group): The groups the ship sprite will be in.

    Attributes:
        num_ships (int): The number of ship objects.
        type_one (dict): The images and animations for ship type one.
        type_two (dict): The images and animations for ship type two.
        type_three (dict): The images and animations for ship type three.
        _ship_type (int): The type of the ship sprite.
        _animation (Animation): The sprites default animation.
        _explosion (Animation): The sprites explosion animation.
        image (pygame.Surface): The image which represents the sprite.
        rect (pygame.Rect): The rect used to place the sprite.
        mask (pygame.mask.Mask): The mask used for collision detection.
        _last_frame (float): The last time the animation was updated.
        _last_shot (float): The last time a shot was fired.
    """
    num_ships = 0

    type_one = {
        'ship': Animation(SpriteSheet.animation(TYPE_ONE, 2), 1, loop=True),
        'bullet': Animation(
            SpriteSheet.animation(TYPE_ONE_BULLET, 2), 0.2, loop=True),
        'explosion': Animation(
            SpriteSheet.animation(TYPE_ONE_EXPLOSION, 1), 0.3),
        'bullet_explosion': Animation(
            SpriteSheet.animation(SHIP_BULLET_EXPLOSION, 1), 0.3)
    }

    type_two = {
        'ship': Animation(SpriteSheet.animation(TYPE_TWO, 2), 1, loop=True),
        'bullet': Animation(
            SpriteSheet.animation(TYPE_TWO_BULLET, 10), 0.05, loop=True),
        'explosion': Animation(
            SpriteSheet.animation(TYPE_TWO_EXPLOSION, 1), 0.3),
        'bullet_explosion': Animation(
            SpriteSheet.animation(SHIP_BULLET_EXPLOSION, 1), 0.3)
    }

    type_three = {
        'ship': Animation(SpriteSheet.animation(TYPE_THREE, 2), 1, loop=True),
        'bullet': Animation(
            SpriteSheet.animation(TYPE_THREE_BULLET, 7), 0.05, loop=True),
        'explosion': Animation(
            SpriteSheet.animation(TYPE_THREE_EXPLOSION, 1), 0.3),
        'bullet_explosion': Animation(
            SpriteSheet.animation(SHIP_BULLET_EXPLOSION, 1), 0.3)
    }

    def __init__(self, ship_type, position, *groups):
        super().__init__(*groups)
        self.__class__.num_ships += 1
        self._ship_type = ship_type

        if self.type == 1:
            self._animation = copy(self.type_one['ship'])
            self._explosion = copy(self.type_one['explosion'])
        elif self.type == 2:
            self._animation = copy(self.type_two['ship'])
            self._explosion = copy(self.type_two['explosion'])
        elif self.type == 3:
            self._animation = copy(self.type_three['ship'])
            self._explosion = copy(self.type_three['explosion'])

        self.image = self._animation.next().convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self._last_frame = 0
        self._reload_speed = 5
        self._last_shot = -(self._reload_speed / 2)

        self.rect.topleft = position

    @property
    def type(self):
        """Get which ship type this sprite is."""
        return self._ship_type

    def update(self, seconds_elapsed):
        """Update the sprites time based variables and if the time is right
        update the sprites animation.

        Arguments:
            seconds_elapsed (float): The time in seconds since the last frame.
        """
        super().update(seconds_elapsed)

        if abs(self._last_frame - self._current_time) >= self._animation.delay:
            self.image = self._animation.next().convert_alpha()
            self.dirty = 1
            self._last_frame = self._current_time

    def shoot(self, tank, *groups):
        """If the ship is not reloading then fire a shot at the tank.

        Arguments:
            tank (Tank): The tank the ships are shooting at.
            groups (pygame.sprite.Group): The groups the bullet will be in.
        """
        if self.rect.x >= tank.rect.x - 50 and self.rect.x <= tank.rect.x + 50:
            if abs(self._last_shot - self._current_time) >= self._reload_speed:
                ShipBullet(self, *groups)
                self._last_shot = self._current_time

    def take_damage(self, bullets, *groups):
        """Check if the ship should be destroyed.

        Arguments:
            bullets (pygame.sprite.Group): The group of bullets.
            groups (pygame.sprite.Group): The groups the explosion will be in.
        """
        for bullet in bullets:
            if pygame.sprite.collide_mask(self, bullet):
                if self._ship_type == 1:
                    Explosion(self._explosion,
                              (self.rect.x - 10, self.rect.y), *groups)
                elif self._ship_type == 2:
                    Explosion(self._explosion,
                              (self.rect.x - 4, self.rect.y), *groups)
                elif self._ship_type == 3:
                    Explosion(self._explosion,
                              (self.rect.x - 2, self.rect.y), *groups)

                bullet.kill()
                self.kill()

    def kill(self):
        """Remove the sprite from all groups and decriment the ship counter."""
        super().kill()
        self.__class__.num_ships -= 1
