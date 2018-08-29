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

from alien_horde import AlienHorde
from constants import DISPLAY, SHIELD, SHIELD_HEIGHT, NUM_SHIELDS, TANK
from shield import Shield
from tank import Tank


class Factory():
    """Class which facilitates the creation of the sprites which are in the
    space invaiders game."""
    @classmethod
    def create_shields(cls, *groups):
        """Create the shields which block bullets.

        Arguments:
            groups (pygame.sprite.Group): The groups the shields will be in.

        Returns:
            list [Shield]: The shields that were created.
        """
        shields = []

        shield_gap = int((DISPLAY.width - NUM_SHIELDS * SHIELD.width) /
                         (NUM_SHIELDS + 1))

        start = shield_gap
        end = DISPLAY.width - SHIELD.width
        step = SHIELD.width + shield_gap

        for pos_x in range(start, end, step):
            shields.append(Shield((pos_x, SHIELD_HEIGHT), *groups))

        return shields

    @classmethod
    def create_tank(cls, *groups):
        """Create the tank that the user controls.

        Arguments:
            groups (pygame.sprite.Group): The groups the shields will be in.

        Returns:
            Tank: The created tank that was created.
        """
        tank_x = DISPLAY.width / 2 - TANK.width / 2
        tank_y = (DISPLAY.height) - TANK.height

        return Tank((tank_x, tank_y), *groups)

    @classmethod
    def create_horde(cls, *groups):
        """Create the alien horde which the user fights.

        Arguments:
            groups (pygame.sprite.Group): The groups the shields will be in.

        Returns:
            AlienHorde: The alien horde which was created.
        """
        return AlienHorde(75, *groups)
