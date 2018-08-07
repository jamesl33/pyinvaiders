#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""


import pygame

from constants import SHIP_TYPE_ONE, \
                      SHIP_TYPE_ONE_BULLET, \
                      SHIP_TYPE_ONE_EXPLOSION, \
                      SHIP_TYPE_TWO, \
                      SHIP_TYPE_TWO_BULLET, \
                      SHIP_TYPE_TWO_EXPLOSION, \
                      SHIP_TYPE_THREE, \
                      SHIP_TYPE_THREE_BULLET, \
                      SHIP_TYPE_THREE_EXPLOSION, \
                      SHIP_TYPE_FOUR, \
                      SHIP_TYPE_FOUR_BULLET, \
                      SHIP_TYPE_FOUR_EXPLOSION
from bullet import Bullet
from explosion import Explosion
from sprite import Sprite
from sprite_sheet import SpriteSheet


class Ship(Sprite):
    """Alien ship which the user gas to shoot down using the Tank.

    Arguments:
        ship_type (int): Determine which ship images to use.
        position (tuple {int, int}): The position to place the ship.
        groups (pygame.sprite.Group): All the groups this sprite will be in.

    Attributes:
        type_one_images (dict): The images used by the first ship sprite.
        type_two_images (dict): The images used by the second ship sprite.
        type_three_images (dict): The images used by the third ship sprite.
        type_four_images (dict): The images used by the fourth ship sprite.
        image (pygame.Surface): The image representing the surface.
        mask (pygame.Mask): The image's mask.
        rect (pygame.Rect): The image's rect.
        reload_speed (int): How long the ship has to wait before firing a shot.
        ship_type (int): Which ship type was used.
    """
    type_one_images = {
        'default': SpriteSheet().load_sprite(SHIP_TYPE_ONE),
        'bullet': SpriteSheet().load_sprite(SHIP_TYPE_ONE_BULLET),
        'explosion': SpriteSheet().load_sprite_strip(SHIP_TYPE_ONE_EXPLOSION,
                                                     1)
    }

    type_two_images = {
        'default': SpriteSheet().load_sprite(SHIP_TYPE_TWO),
        'bullet': SpriteSheet().load_sprite(SHIP_TYPE_TWO_BULLET),
        'explosion': SpriteSheet().load_sprite_strip(SHIP_TYPE_TWO_EXPLOSION,
                                                     1)
    }

    type_three_images = {
        'default': SpriteSheet().load_sprite(SHIP_TYPE_THREE),
        'bullet': SpriteSheet().load_sprite(SHIP_TYPE_THREE_BULLET),
        'explosion': SpriteSheet().load_sprite_strip(SHIP_TYPE_THREE_EXPLOSION,
                                                     1)
    }

    type_four_images = {
        'default': SpriteSheet().load_sprite(SHIP_TYPE_FOUR),
        'explosion': SpriteSheet().load_sprite_strip(SHIP_TYPE_FOUR_EXPLOSION,
                                                     1)
    }

    def __init__(self, ship_type, position, *groups):
        super().__init__(*groups)
        if ship_type == 1:
            self.images = self.type_one_images
        elif ship_type == 2:
            self.images = self.type_two_images
        elif ship_type == 3:
            self.images = self.type_three_images
        elif ship_type == 4:
            self.images = self.type_four_images

        self.image = self.images['default'].convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.reload_speed = 5
        self.ship_type = ship_type

        self.rect.x, self.rect.y = position

    def shoot(self, ship, *groups):
        """If the ship is not reloading then fire a shot.

        Arguments:
            ship (Ship): The ship sprite which fired the bullet.
            groups (pygame.sprite.Group): The groups the bullet will be put in.
        """
        if self.ship_type == 4:
            return

        if self.rect.x >= ship.rect.x - 50 and self.rect.y <= ship.rect.x + 50:
            if self.current_time >= self.reload_speed:
                pos_x = self.rect.x + self.rect.width / 2 - \
                    self.images['bullet'].get_rect().width / 2
                pos_y = self.rect.y + self.rect.height

                Bullet(self.images['bullet'],
                       (pos_x, pos_y),
                       pygame.math.Vector2(0, -750),
                       *groups)

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
                explosion = Explosion(self.images['explosion'],
                                      (self.rect.x, self.rect.y), 0.3, *groups)
                # TODO remove these hardcoded values.
                if self.ship_type == 1:
                    explosion.rect.x -= 10
                elif self.ship_type == 2:
                    explosion.rect.x -= 4
                elif self.ship_type == 3:
                    explosion.rect.x -= 2
                elif self.ship_type == 4:
                    explosion.rect.x += 6

                bullet.kill()
                self.kill()
