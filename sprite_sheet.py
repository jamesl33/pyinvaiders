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

import pygame

from constants import SPRITE_SHEET


class SpriteSheet():
    """Allow the fetching of sprites from an external sprite sheet."""
    try:
        sheet = pygame.image.load(SPRITE_SHEET)
    except pygame.error:
        print('Error: Failed to open sprite sheet')
        exit()

    @classmethod
    def sprite(cls, rect):
        """Fetch a single sprite from the sprite sheet.

        Arguments:
            rect (pygame.Rect): The rect for the sprite you are trying to get.

        Returns:
            pygame.Surface: A surface containing the sprite.
        """
        return cls.sheet.subsurface(rect)

    @classmethod
    def animation(cls, rect, count):
        """Get a list of surfaces containg sprites which can be used to create
        animations.

        Arguments:
            rect (pygame.Rect): The rect which contains the first frame.
            count (int): The amount of frames to extract.

        Returns:
            list [pygame.Surface]: A list containing a surface for each frame.
        """
        animation = []
        rect = rect.copy()

        for _ in range(count):
            animation.append(cls.sprite(rect))
            rect.x += rect.width + 4

        return animation
