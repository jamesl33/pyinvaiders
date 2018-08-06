#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

from constants import DISPLAY
from sprite import Sprite


class Bullet(Sprite):
    """A base class for any type of bullet.

    Arguments:
        groups (pygame.sprite.Group): All the groups this sprite will be in.

    Attributes:
        damage (int): The damage that the bullet will case on inpact.
    """
    def __init__(self, *groups):
        super().__init__(*groups)
        self.damage = None

    def move(self):
        """Update the bullets position depending on the objects time based
        variables."""
        self.rect.y -= int(self.seconds_elapsed * self.velocity.y)

        if not self.rect.colliderect(DISPLAY):
            self.kill()
