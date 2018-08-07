#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""


import pygame

from sprite import Sprite
from ship_explosion import ShipExplosion
from ship_bullet import ShipBullet


class Ship(Sprite):
    """Alien ship which the user gas to shoot down using the Tank.

    Arguments:
        image (pygame.Surface): The image representing the sprite.
        groups (pygame.sprite.Group): All the groups this sprite will be in.

    Attributes:
        image (pygame.Surface): The image representing the surface.
        mask (pygame.Mask): The image's mask.
        rect (pygame.Rect): The image's rect.
        reload_speed (int): How long the ship has to wait before firing a shot.
    """
    def __init__(self, image, *groups):
        super().__init__(*groups)
        self.image = image.convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.reload_speed = 5

    def shoot(self, ship, *groups):
        """If the ship is not reloading then fire a shot.

        Arguments:
            ship (Ship): The ship sprite which fired the bullet.
            groups (pygame.sprite.Group): The groups the bullet will be put in.
        """
        if self.rect.x >= ship.rect.x - 50 and self.rect.y <= ship.rect.x + 50:
            if self.current_time >= self.reload_speed:
                ShipBullet(self, *groups)
                self.current_time = 0

    def take_damage(self, bullets, *groups):
        """If there are any bullets in contact with the ship take destroy the
        ship.

        Arguments:
            bullets (pygame.sprite.Group): A group of bullet sprite objects.
            groups (pygame.sprite.Group): The groups to add the explosion to.
        """
        for bullet in bullets:
            if pygame.sprite.collide_mask(self, bullet):
                if self.rect.width % 2 == 0:
                    explosion = ShipExplosion(self, *groups)
                    explosion.rect.x -= 10
                else:
                    ShipExplosion(self, *groups)

                bullet.kill()
                self.kill()
