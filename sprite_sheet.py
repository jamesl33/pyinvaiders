#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""


import pygame


class SpriteSheet():
    """Allow the fetching of sprites from an external sprite sheet."""
    sprite_sheet = pygame.image.load('assets/images/sprite-sheet.png')

    @staticmethod
    def load_sprite(rect):
        """Get a single image from a sprite sheet.

        Arguments:
            rect (pygame.Rect): The rect which contains the sprite.

        Returns:
            sprite (pygame.Surface): The extracted image.
        """
        sprite = SpriteSheet.sprite_sheet.subsurface(rect)

        return sprite

    @staticmethod
    def load_sprite_strip(rect, count):
        """Get a strip of images form a sprite sheet.

        Arguments:
            rect (pygame.Rect): The rect which contains the sprite.
            count (int): The amount of sprites in the strip.

        Returns:
            sprite_strip (iter [pygame.Surface]): The extracted sprite strip.
        """
        sprite_strip = []

        for _ in range(count):
            sprite_strip.append(SpriteSheet.sprite_sheet.subsurface(rect))
            rect.x += rect.w

        return iter(sprite_strip)
