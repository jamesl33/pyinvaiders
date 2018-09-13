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
