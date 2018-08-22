#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
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
