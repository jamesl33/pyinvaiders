#!/usr/bin/env python3
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

from random import sample, randint

from alien_horde_layer import AlienHordeLayer
from constants import (DISPLAY, HORDE_WIDTH, HORDE_BUFFER, TYPE_ONE, TYPE_TWO,
                       TYPE_THREE)
from ship import Ship
from mystery import Mystery


class AlienHorde():
    """Class which represets the alien horde which has come to attack the user
    playing as the tank.

    Arguments:
        height (int): what height to place the horde.
        groups (pygame.sprite.Group): The groups the ships will be in.

    Attributes:
        _current_time (float): Time since the objects creation.
        _seconds_elapsed (float): The seconds elapsed since the last frame.
        _layers (list): The layers that make up the horde.
        _speed_multiplier (float): The multiplier used to speed up the ships.
        _shooting_delay (float): The amount of time to wait before shooting.
        _last_shots (float): The time when shots were last fired.
        _last_move (float): The time the horde last moved.
        _current_layer (int): The layer index in _layers.
        _ship_count (int): The amount of ships left in the horde.
    """
    def __init__(self, height, *groups):
        self._current_time = 0
        self._seconds_elapsed = 0
        self._layers = []
        self._speed_multiplier = 0
        self._shooting_delay = 0.5
        self._last_shots = 0
        self._last_move = 0
        self._last_mystery = 0
        self._mystery_time = randint(10, 30)
        self._ship_groups = groups

        for _ in range(5):
            self._layers.append(AlienHordeLayer())

        self._current_layer = len(self._layers) - 1

        ship_gap = int(((DISPLAY.width - HORDE_BUFFER * 2) -
                        (HORDE_WIDTH * TYPE_THREE.width)) / (HORDE_WIDTH + 1))
        start = ship_gap
        end = DISPLAY.width - TYPE_THREE.width
        step = TYPE_THREE.width + ship_gap

        for pos_x in range(start + HORDE_BUFFER, end - HORDE_BUFFER, step):
            self._layers[0].append(Ship(1, (int(pos_x + (TYPE_THREE.width / 2) - (TYPE_ONE.width / 2)), height), self._ship_groups))
            self._layers[1].append(Ship(2, (int(pos_x + (TYPE_THREE.width / 2) - (TYPE_TWO.width / 2)), height + 50), self._ship_groups))
            self._layers[2].append(Ship(2, (int(pos_x + (TYPE_THREE.width / 2) - (TYPE_TWO.width / 2)), height + 100), self._ship_groups))
            self._layers[3].append(Ship(3, (pos_x, height + 150), self._ship_groups))
            self._layers[4].append(Ship(3, (pos_x, height + 200), self._ship_groups))

        self._ship_count = Ship.num_ships

    def update(self, seconds_elapsed):
        """Update the horde's time based variables and do any animation work.

        Arguments:
            seconds_elapsed (float): The seconds elspased since the last frame.
        """
        self._current_time += seconds_elapsed
        self._seconds_elapsed = seconds_elapsed

        for layer in self._layers:
            layer.update(seconds_elapsed)

        if self._ship_count == 1:
            self._speed_multiplier = 2

        ship_count = Ship.num_ships

        if ship_count < self._ship_count:
            self._speed_multiplier += (self._ship_count - ship_count) / 250
            self._ship_count = ship_count

        if abs(self._last_mystery - self._current_time) >= self._mystery_time:
            Mystery(randint(0, 1), self._ship_groups)
            self._last_mystery = self._current_time

    def move(self):
        """Move the ships one layer at a time. The speed that they move will
        change as more ships are shot down. This is according to
        _speed_multiplier.
        """
        if self._current_layer < 0:
            self._current_layer = len(self._layers) - 1

        if abs(self._last_move - self._current_time) >= 0.2 - self._speed_multiplier:
            self._layers[self._current_layer].move()
            self._current_layer -= 1
            self._last_move = self._current_time

    def shoot(self, tank, *groups):
        """Randomly fire shots at the tank as long as there isn't any ships
        below the one that is firing.

        Arguments:
            tank (Tank): The tank which the ships are shooting at.
            groups (pygame.sprite.Group): The groups the bullets will be in.
        """
        def _shoot_colummn(column):
            for index in range(len(self._layers) - 1, -1, -1):
                if self._layers[index][column].alive():
                    self._layers[index][column].shoot(tank, *groups)
                    return

        if abs(self._last_shots - self._current_time) >= self._shooting_delay:
            for column in sample(range(0, HORDE_WIDTH), int(HORDE_WIDTH / 2)):
                _shoot_colummn(column)
            self._last_shots = self._current_time
