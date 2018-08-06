#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

# pylint: disable-msg=E1121

import pygame

from constants import DISPLAY, FPS, SHIELD, NUM_SHIELDS
from shield import Shield
from tank import Tank


class SpaceInvaiders():
    """A clone of the classic Space Invaders game built using Python 3 and
    pygame.

    Attributes:
        background (pygame.Surface): The background surface.
        clock (pygame.time.Clock): The games clock.
        display (pygame.display): The games main display.
        sprites (dict {pygame.sprite.LayeredDirty}): All the games sprites.
        tank (Tank): The tank that the user controls.
    """
    def __init__(self):
        self.background = pygame.Surface(DISPLAY.size)
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(DISPLAY.size)
        self.sprites = {
            'all': pygame.sprite.LayeredDirty(),
            'tanks': pygame.sprite.LayeredDirty(),
            'bullets': pygame.sprite.LayeredDirty(),
            'shields': pygame.sprite.LayeredDirty()
        }
        self.tank = None

    def start(self):
        """This function is called to start the game."""
        self.restart()

        while True:
            self._update()

    def restart(self):
        """Restart the game resetting the games variables to their default
        values."""
        for _, sprite_group in self.sprites.items():
            sprite_group.empty()

        self.tank = Tank(self.sprites['all'], self.sprites['tanks'])

        gap = int((DISPLAY.width - NUM_SHIELDS * SHIELD.width) /
                  (NUM_SHIELDS + 1))
        shield_height = DISPLAY.height - (SHIELD.height * 2)
        shield_groups = self.sprites['all'], self.sprites['shields']

        for pos_x in range(gap, DISPLAY.width -
                           SHIELD.width, SHIELD.width + gap):
            Shield((pos_x, shield_height), shield_groups)

    def _update(self):
        """Progress the game by a single frame."""
        self._clear_sprites()
        self._update_sprites(self.clock.tick(FPS) / 1000)
        self._handle_input(pygame.key.get_pressed())
        self._draw_sprites(self.sprites['all'].draw(self.display))

    def _clear_sprites(self):
        """Draw the background over all the sprites."""
        self.sprites['all'].clear(self.display, self.background)

    def _update_sprites(self, seconds_elapsed):
        """Update all the sprites timed based variables and do any operations
        which involve updating the sprites"""
        self.sprites['all'].update(seconds_elapsed)

        for bullet in self.sprites['bullets']:
            bullet.move()

        for shield in self.sprites['shields']:
            shield.take_damage(self.sprites['bullets'])

    def _handle_input(self, keys):
        """Handle any input from the user."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        self.tank.move(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])

        if keys[pygame.K_UP]:
            self.tank.shoot(self.sprites['all'], self.sprites['bullets'])

    @classmethod
    def _draw_sprites(cls, dirty_rects):
        """Redraw the sprites on the display."""
        pygame.display.update(dirty_rects)


if __name__ == '__main__':
    GAME = SpaceInvaiders()
    GAME.start()
