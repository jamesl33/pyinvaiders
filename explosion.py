#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

from sprite import Sprite


class Explosion(Sprite):
    """Sprite which is some form of explosion. Such as when a ship or tank is
    hit by a bullet.

    Arguments:
        animation (Animation): The animation for the explosion.
        position (tuple {int, int}): The x, y position to place the sprite.
        animation_speed (float): How long to wait before progressing a frame.
        groups (pygame.sprite.Group): All the groups this sprite will be in.

    Attributes:
        animation (Animation): The animation for the explosion.
        image (pygame.Surface): The image representing the sprite.
        last_frame_time (float): The last time a frame was processed.
        rect (pygame.Rect): The rect for the image surface.
    """
    def __init__(self, animation, position, *groups):
        super().__init__(*groups)
        self.animation = animation
        self.image = self.animation.next()
        self.last_frame_time = 0
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = position

    def update(self, seconds_elapsed):
        """Update the animation for the explosion.

        Arguments:
            seconds_elapsed (float): Time since last from was drawn.
        """
        super().update(seconds_elapsed)

        if self.last_frame_time - self.current_time <= -self.animation.animation_speed:
            next_frame = self.animation.next()

            if next_frame is None:
                self.kill()

            self.image = next_frame
            self.last_frame_time = self.current_time
            self.dirty = 1
