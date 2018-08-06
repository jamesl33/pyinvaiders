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
        groups (pygame.sprite.Group): All the groups this sprite will be in.

    Attributes:
        images (list): The frames which make up the animation.
        image (pygame.Surface): The image representing the sprite.
        rect (pygame.Rect): The rect for the image surface.
    """
    def __init__(self, images, *groups):
        super().__init__(*groups)
        self.images = iter(images)
        self.image = next(self.images)
        self.rect = self.image.get_rect()

    def update(self, seconds_elapsed):
        """Update the animation for the explosion.

        Arguments:
            seconds_elapsed (float): Time since last from was drawn.
        """
        super().update(seconds_elapsed)

        if self.current_time >= self.animation_speed:
            try:
                self.image = next(self.images)
            except StopIteration:
                self.kill()

            self.dirty = 1
