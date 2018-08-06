#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

import pygame


class Sprite(pygame.sprite.DirtySprite):
    """A simple extension to the pygame sprite class which makes time based
    movement easier.

    Arguments:
        groups (pygame.sprite.Group): All the groups this sprite will be in.

    Attributes:
        current_time (float): Time since the last time based event.
        dirty (int): Determine if the sprite should be redrawn or not.
        seconds_elapsed (float): Time since the last frame was drawn.
    """
    def __init__(self, *groups):
        super().__init__(*groups)
        self.current_time = 0
        self.dirty = 1
        self.seconds_elapsed = 0

    def update(self, seconds_elapsed):
        """Update the sprites time based variables.

        Arguments:
            seconds_elapsed (float): Time since last from was drawn.
        """
        self.current_time += seconds_elapsed
        self.seconds_elapsed = seconds_elapsed
