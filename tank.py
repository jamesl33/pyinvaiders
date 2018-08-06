#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

import pygame

from constants import DISPLAY, TANK
from sprite import Sprite
from sprite_sheet import SpriteSheet
from tank_bullet import TankBullet
from tank_explosion import TankExplosion


class Tank(Sprite):
    """The tank which the user controls to fight the alien horde.

    Arguments:
        groups (pygame.sprite.Group): All the groups this sprite will be in.

    Attributes:
        current_time (int): Allow tank to fire from the start of the game.
        image (pygame.Surface): The image representing the sprite.
        mask (pygame.Mask): Mask used for precise collison detection.
        rect (pygame.Rect): The rect for the image surface.
        reload_speed (float): The amount of time to wait before fireing a shot.
        velocity (pygame.math.Vector2): Movement velocity in the x, y axis.
    """
    image = SpriteSheet().load_sprite(TANK)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.current_time = 1
        self.image = self.image.convert_alpha()
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
        if self.current_time >= self.reload_speed:
            TankBullet(self, *groups)
            self.current_time = 0

    def take_damage(self, bullets, *groups):
        """Check if there is a collision with an ememy bullet. If there is
        destroy the tank and create a TankExplosion sprite.

        Arguments:
            bullets (pygame.sprite.Group): The group containing bullet sprites.
            groups (pygame.sprite.Group): The groups the explosion will be in.
        """
        for bullet in bullets:
            if pygame.sprite.collide_mask(self, bullet):
                bullet.kill()
                TankExplosion(self, *groups)
                self.kill()
