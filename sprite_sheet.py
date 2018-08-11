#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
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
