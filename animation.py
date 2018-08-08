#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""


class Animation():
    """A simple animation class which allows the manipulation of animations
    which are loaded into a list of frames.

    Arguments:
        frames (list [pygame.Surface]): The frames that make up the animation.
        animation_speed (float): The amount of time to wait between each frame.
        loop (bool): Should the animation loop.

    Attributes:
        animation_speed (float): The amount of time to wait between each frame.
        frame (int): The current frame in the frames list.
        frames (list [pygame.Surface]): The frames that make up the animation.
        loop (bool): Whether or not this animation is looping.
    """
    def __init__(self, frames, animation_speed, loop=False):
        self.animation_speed = animation_speed
        self.frame = 0
        self.frames = frames
        self.loop = loop

    def next(self):
        """Get the next frame of the animation."""
        try:
            frame = self.frames[self.frame]
        except IndexError:
            if self.loop:
                self.frame = 0
                frame = self.frames[self.frame]
            else:
                frame = None

        self.frame += 1
        return frame
