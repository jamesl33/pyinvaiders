#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""


class Animation():
    """Make using animations loaded from the sprite sheet easier to use.

    Arguments:
        frames (list [pygame.Surface]): The frames that make up the animation.
        delay (float): The amount of time between each frame.
        loop (bool): If the animation should loop or not.

    Attributes:
        _frames (list [pygame.Surface]): The frames that make up an animation.
        _delay (float): The time between each frame.
        _loop (bool): If the animation should loop or not.
        _current_frame (int): The index of the current frame in _frames.
    """
    def __init__(self, frames, delay, loop=False):
        self._frames = frames
        self._delay = delay
        self._loop = loop
        self._current_frame = 0

    @property
    def delay(self):
        """Get the frame delay value for the animation.

        Returns:
            float: The amount of time between each of the frames.
        """
        return self._delay

    def next(self):
        """Get the next frame from the animation.

        Returns:
            pygame.Surface: The next sprite frame in the animation.
        """
        try:
            frame = self._frames[self._current_frame]
            self._current_frame += 1
            return frame
        except IndexError:
            if self._loop:
                self._current_frame = 0
                return self.next()
