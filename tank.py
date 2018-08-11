#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

from copy import copy

import pygame

from animation import Animation
from constants import DISPLAY, \
                      TANK, \
                      TANK_BULLET, \
                      TANK_EXPLOSION, \
                      TANK_BULLET_EXPLOSION
from entity import Entity
from explosion import Explosion
from sprite_sheet import SpriteSheet
from tank_bullet import TankBullet


class Tank(Entity):
    """The tank which the user controls to destroy the oncoming alien horde.

    Arguments:
        groups (pygame.sprite.Group): All the groups this entity will be in.

    Attributes:
        tank (pygame.Surface): The default sprite for the tank.
        bullet (pygame.Surface): The tanks bullet sprite.
        explosion (pygame.Surface): The tanks explosion animation.
        image (pygame.Surface): The current image which represents the sprite.
        rect (pygame.Rect): The rect used for placing the sprite.
        mask (pygame.mask.Mask): The mast for the image.
        _velocity (pygame.math.Vector2): The x, y velocities for the sprite.
        _last_shot (float): The last time that the tank fired a shot.
        _reload_speed (float): The amount of time it takes to reload.
        _current_time (float): Time in seconds. (Used for time based actions)
    """
    tank = SpriteSheet.sprite(TANK)
    bullet = SpriteSheet.sprite(TANK_BULLET)
    explosion = Animation(SpriteSheet.animation(TANK_EXPLOSION, 1), 0.3)
    bullet_explosion = Animation(
        SpriteSheet.animation(TANK_BULLET_EXPLOSION, 1), 0.3)

    def __init__(self, position, *groups):
        super().__init__(*groups)
        self.image = copy(self.tank).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self._velocity = pygame.math.Vector2(250, 0)
        self._last_shot = 0
        self._reload_speed = 0.5
        self._current_time = self._reload_speed

        self.rect.topleft = position

    def move(self, direction):
        """Move the tank according the users input.

        Arguments:
            The direction to move the tank. left < 0 > right.
        """
        velocity = int(self._seconds_elapsed * self._velocity.x)

        if direction != 0:
            self.dirty = 1
        if direction < 0 and self.rect.left > velocity:
            self.rect.x -= velocity
        elif direction > 0 and self.rect.right < DISPLAY.height - velocity:
            self.rect.x += velocity

    def shoot(self, *groups):
        """If the tank isn't reloading then fire a shot.

        Arguments:
            groups (pygame.sprite.Group): The groups the bullet will be in.
        """
        if abs(self._last_shot - self._current_time) >= self._reload_speed:
            TankBullet(self, *groups)
            self._last_shot = self._current_time

    def take_damage(self, bullets, *groups):
        """Tank damage from any of the bullets on the display.

        Arguments:
            bullets (pygame.sprite.Group): The bullet group.
            groups (pygame.sprite.Group): The groups the explosion will be in.
        """
        for bullet in bullets:
            if pygame.sprite.collide_mask(self, bullet):
                Explosion(copy(self.explosion),
                          (self.rect.x - 4, self.rect.y),
                          *groups)

                bullet.kill()
                self.kill()
