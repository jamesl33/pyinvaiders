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

from entity import Entity
from animation import Animation


class Explosion(Entity):
    """A sprite which displays a explosion animation for another sprite. This
    sprite is commenly creation on the death of another sprite.

    Arguments:
        animation (Animation): The animation for the explosion.
        position (tuple {int, int}): Where to place the sprite.

    Attributes:
        _animation (Animation): The animation for the explosion.
        _last_frame (float): The time when the last frame was drawn.
        image (pygame.Surface): The current image which represents the sprite.
        rect (pygame.Rect): The rect used for placing the sprite.
    """
    def __init__(self, animation, position, *groups):
        super().__init__(*groups)
        self._animation = animation
        self._last_frame = 0
        self.image = self._animation.next().convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.topleft = position

    def update(self, seconds_elapsed):
        """Advance the explosions animation depending if its the right time to
        do so.

        Arguments:
            seconds_elapsed (float): The time since the last frame was drawn.
        """
        super().update(seconds_elapsed)

        if abs(self._last_frame - self._current_time) >= self._animation.delay:
            next_frame = self._animation.next()

            if next_frame is None:
                self.kill()
            else:
                self.image = next_frame.convert_alpha()
                self._last_frame = self._current_time
                self.dirty = 1
