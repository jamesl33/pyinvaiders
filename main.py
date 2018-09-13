#!/usr/bin/env python3
"""
This file is part of pyinvaiders.

Copyright (C) 2018, James Lee <jamesl33info@gmail.com>.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

# pylint: disable-msg=E1121

import pygame

from constants import FPS, DISPLAY, BACKGROUND
from factory import Factory


class SpaceInvaiders():
    """A clone of the classic Space Invaiders game.

    Attributes:
        _display (pygame.display): The main display surface.
        _background (pygame.Surface): The games background surface.
        _clock (pygame.time.Clock): The games main clock.
        _tank (Tank): The tank the user controls.
        _shields (list [Shield]): The shields which defend the user.
        _alien_horde (AlienHorde): The alien horde which the user fights.
        _entities (dict {pygame.sprite.Group}): The groups of entities.
    """
    def __init__(self):
        self._display = pygame.display.set_mode(DISPLAY.size)
        self._background = pygame.Surface(BACKGROUND.size)
        self._clock = pygame.time.Clock()
        self._tank = None
        self._shields = None
        self._alien_horde = None
        self._entities = {
            'all': pygame.sprite.LayeredDirty(),
            'bullets': pygame.sprite.LayeredDirty(),
            'explosions': pygame.sprite.LayeredDirty(),
            'mystery': pygame.sprite.LayeredDirty(),
            'shields': pygame.sprite.LayeredDirty(),
            'ship_bullets': pygame.sprite.LayeredDirty(),
            'ships': pygame.sprite.LayeredDirty(),
            'tank_bullets': pygame.sprite.LayeredDirty(),
            'tanks': pygame.sprite.LayeredDirty()
        }

    def start(self):
        """Start playing the game."""
        self.restart()

        while True:
            self._update()

    def restart(self):
        """Reset all the games variables causing a restart."""
        for _, sprite_group in self._entities.items():
            sprite_group.empty()

        self._tank = Factory.create_tank(self._entities['all'],
                                         self._entities['tanks'])
        self._shields = Factory.create_shields(self._entities['all'],
                                               self._entities['shields'])
        self._alien_horde = Factory.create_horde(self._entities['all'],
                                                 self._entities['ships'])

    def _update(self):
        """Update the game by one frame."""
        self._clear_entities()
        self._update_entities(self._clock.tick(FPS) / 1000)
        self._handle_input(pygame.key.get_pressed())
        self._draw_entities(self._entities['all'].draw(self._display))

    def _clear_entities(self):
        """Clear all of the sprites on the display"""
        self._entities['all'].clear(self._display, self._background)

    def _update_entities(self, seconds_elapsed):
        """Do any operations which will update the games state.

        Arguments:
            seconds_elapsed (float): The time in seconds since the last frame.
        """
        self._entities['all'].update(seconds_elapsed)

        self._alien_horde.update(seconds_elapsed)

        self._tank.take_damage(self._entities['ship_bullets'],
                               self._entities['all'],
                               self._entities['explosions'])

        self._alien_horde.move()

        self._alien_horde.shoot(self._tank,
                                self._entities['all'],
                                self._entities['bullets'],
                                self._entities['ship_bullets'])

        for sheild in self._entities['shields']:
            sheild.take_damage(self._entities['bullets'])

        for ship in self._entities['ships']:
            ship.take_damage(self._entities['tank_bullets'],
                             self._entities['all'],
                             self._entities['explosions'])

        for mystery in self._entities['mystery']:
            mystery.take_damage(self._entities['tank_bullets'],
                                self._entities['all'],
                                self._entities['explosions'])

        for bullet in self._entities['bullets']:
            bullet.take_damage(self._entities['bullets'],
                               self._entities['all'],
                               self._entities['explosions'])

    def _handle_input(self, keys):
        """Handle any of the keys pressed by the user.

        Arguments:
            keys (dict {int: bool}): The keys which are currently pressed.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if keys[pygame.K_LCTRL] and keys[pygame.K_r]:
            self.restart()

        self._tank.move(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])

        if keys[pygame.K_UP]:
            self._tank.shoot(self._entities['all'],
                             self._entities['bullets'],
                             self._entities['tank_bullets'])

    @classmethod
    def _draw_entities(cls, dirty_rects):
        """Redraw any of the entities which were cleared.

        Arguments:
            dirty_rects (list [pygame.Rect]): The rects to redraw.
        """
        pygame.display.update(dirty_rects)


if __name__ == '__main__':
    GAME = SpaceInvaiders()
    GAME.start()
