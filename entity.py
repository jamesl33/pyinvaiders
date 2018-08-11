#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

import pygame


class Entity(pygame.sprite.DirtySprite):
    """Every entity should have these time based variables which allow for
    time based animation. This avoids having to limit the frame rate.

    Arguments:
        groups (pygame.sprite.Group): All the groups this entity will be in.

    Attributes:
        dirty (int): Wether or not the sprite should be drawn.
        _current_time (float): Time in seconds. (Used for time based actions)
        _seconds_elapsed (float): The time since the last frame was drawn.
    """
    def __init__(self, *groups):
        super().__init__(*groups)
        self.dirty = 1
        self._current_time = 0
        self._seconds_elapsed = 0

    def update(self, seconds_elapsed):
        """Update the entities time based variables.

        Arguments:
            seconds_elapsed (float): The time since the last frame was drawn.
        """
        self._current_time += seconds_elapsed
        self._seconds_elapsed = seconds_elapsed
