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
        images (list): The frames which make up the animation.
        position (tuple {int, int}): The x, y position to place the sprite.
        animation_speed (float): How long to wait before progressing a frame.
        groups (pygame.sprite.Group): All the groups this sprite will be in.

    Attributes:
        animation_speed (float): How long to wait before progressing a frame.
        images (list): The frames which make up the animation.
        image (pygame.Surface): The image representing the sprite.
        last_frame_time (float): The last time a frame was processed.
        rect (pygame.Rect): The rect for the image surface.
    """
    def __init__(self, images, position, animation_speed, *groups):
        super().__init__(*groups)
        self.animation_speed = animation_speed
        self.images = iter(images)
        self.image = next(self.images)
        self.last_frame_time = 0
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = position

    def update(self, seconds_elapsed):
        """Update the animation for the explosion.

        Arguments:
            seconds_elapsed (float): Time since last from was drawn.
        """
        super().update(seconds_elapsed)

        if self.last_frame_time - self.current_time <= -self.animation_speed:
            try:
                self.image = next(self.images)
            except StopIteration:
                self.kill()

            self.last_frame_time = self.current_time
            self.dirty = 1
