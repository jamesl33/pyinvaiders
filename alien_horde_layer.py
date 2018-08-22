#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

import pygame

from ship import Ship
from constants import DISPLAY, HORDE_WIDTH, TYPE_ONE, TYPE_TWO, TYPE_THREE


class AlienHordeLayer():
    """One of the layers in the alien horde.

    Attributes:
        _current_time (float): The time since the layer was created.
        _seconds_elapsed (float): The time since the last frame was drawn.
        _ships (list [Ship]): The list of ships in the layer.
        _current_ship (Ship): The ship currently being moved.
        _velocity (pygame.math.Vector2): The speed which the ships move.
        _last_move (float): The last time a move was made.
    """
    def __init__(self):
        self._current_time = 0
        self._seconds_elapsed = 0
        self._ships = []
        self._current_ship = None
        self._velocity = pygame.math.Vector2(10, 0)
        self._last_move = 0

    def update(self, seconds_elapsed):
        """Update the time base variables. Make sure that the ships don't
        all drop to the next layer at once. They should fall on after
        another.

        Arguments:
            seconds_elapsed (float): The time since the last frame was drawn.
        """
        self._current_time += seconds_elapsed
        self._seconds_elapsed = seconds_elapsed

        if self._velocity.y != 0:
            if self._current_ship is None:
                if self._velocity.x < 0:
                    self._current_ship = 0
                else:
                    self._current_ship = len(self._ships) - 1

            if self._current_ship < 0 or self._current_ship >= HORDE_WIDTH:
                self._current_ship = None
                self._last_move = 0
                self._velocity.y = 0
                return

            if abs(self._last_move - self._current_time) >= 0.05:
                self._ships[self._current_ship].rect.y += self._velocity.y
                self._ships[self._current_ship].dirty = 1

                if self._velocity.x < 0:
                    self._current_ship += 1
                else:
                    self._current_ship -= 1

                self._last_move = self._current_time

    def move(self):
        """Move the ships and make sure that they do not disappear of the
        screen.
        """
        if self._ships[0].type == 1:
            ship_buffer = TYPE_ONE.width
        elif self._ships[0].type == 2:
            ship_buffer = (TYPE_TWO.width / 2) + (TYPE_TWO.width / 8)
        elif self._ships[0].type == 3:
            ship_buffer = TYPE_THREE.width / 2

        if Ship.num_ships != 1:
            for ship in self._ships:
                if ship.rect.left <= 0 + ship_buffer:
                    self._velocity.x = abs(self._velocity.x)
                    self._velocity.y = 20
                elif ship.rect.right >= DISPLAY.width - ship_buffer:
                    self._velocity.x = -self._velocity.x
                    self._velocity.y = 20
        else:
            for ship in [ship for ship in self._ships if ship.alive()]:
                if ship.rect.left <= 0 + ship_buffer:
                    self._velocity.x = abs(self._velocity.x)
                    self._velocity.y = 20
                elif ship.rect.right >= DISPLAY.width - ship_buffer:
                    self._velocity.x = -self._velocity.x
                    self._velocity.y = 20

        for ship in self._ships:
            ship.rect.x += self._velocity.x
            ship.dirty = 1

    def append(self, ship):
        """Add a new ship to the layer.

        Arguments:
            ship (Ship): The ship being added to the layer.
        """
        self._ships.append(ship)

    def __getitem__(self, index):
        """Allow the layer to be indexed. The is used when making the ships
        shoot at the tank.

        Arguments:
            index (int): The index that the user wants.
        """
        return self._ships[index]
