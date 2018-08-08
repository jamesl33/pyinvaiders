#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

import pygame

from bullet import Bullet
from constants import DISPLAY, TANK, TANK_BULLET, TANK_EXPLOSION
from explosion import Explosion
from sprite import Sprite
from sprite_sheet import SpriteSheet


class Tank(Sprite):
    """The tank which the user controls to fight the alien horde.

    Arguments:
        groups (pygame.sprite.Group): All the groups this sprite will be in.

    Attributes:
        images (dict {pygame.Surface}): The images used by the tank sprite.
        current_time (int): Allow tank to fire from the start of the game.
        image (pygame.Surface): The image which represents the sprite.
        last_shot_time (float): The last time the tank fired a bullet.
        mask (pygame.Mask): Mask used for precise collison detection.
        rect (pygame.Rect): The rect for the image surface.
        reload_speed (float): The amount of time to wait before fireing a shot.
        velocity (pygame.math.Vector2): Movement velocity in the x, y axis.
    """
    images = {
        'default': SpriteSheet().load_sprite(TANK),
        'bullet': SpriteSheet().load_sprite(TANK_BULLET),
        'explosion': SpriteSheet().load_sprite_strip(TANK_EXPLOSION, 1)
    }

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = self.images['default'].convert_alpha()
        self.last_shot_time = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.reload_speed = 0.5
        self.velocity = pygame.math.Vector2(250, 0)

        self.rect.x = DISPLAY.width / 2 - self.rect.width / 2
        self.rect.y = (DISPLAY.height - self.rect.height)

    def move(self, direction):
        """Move the Tank sprite according to the direction.

        Arguments:
            direction (int): The direction to move. left < 0 > right.
        """
        incriment = int(self.seconds_elapsed * self.velocity.x)

        if direction != 0:
            self.dirty = 1
        if direction < 0 and self.rect.left > incriment:
            self.rect.x -= incriment
        elif direction > 0 and self.rect.right < DISPLAY.height - incriment:
            self.rect.x += incriment

    def shoot(self, *groups):
        """Fire a bullet from the Tank's cannon.

        Arguments:
            groups (pygame.sprite.Group): The groups the bullet will be in.
        """
        if self.last_shot_time - self.current_time <= -self.reload_speed:
            pos_x = TANK_BULLET.x = self.rect.x + self.rect.width / 2 - \
                TANK_BULLET.width / 2
            pos_y = TANK_BULLET.y = self.rect.y - TANK_BULLET.height

            Bullet(self.images['bullet'], (pos_x, pos_y),
                   pygame.math.Vector2(0, 750), *groups)

            self.last_shot_time = self.current_time

    def take_damage(self, bullets, *groups):
        """Check if there is a collision with an ememy bullet. If there is
        destroy the tank and create a TankExplosion sprite.

        Arguments:
            bullets (pygame.sprite.Group): The group containing bullet sprites.
            groups (pygame.sprite.Group): The groups the explosion will be in.
        """
        for bullet in bullets:
            if pygame.sprite.collide_mask(self, bullet):
                Explosion(self.images['explosion'],
                          (self.rect.x - 4, self.rect.y), 0.5, *groups)
                bullet.kill()
                self.kill()
