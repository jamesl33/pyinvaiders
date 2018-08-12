#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

# pylint: disable-msg=E1121

import pygame

from constants import FPS, DISPLAY, BACKGROUND, TANK, SHIELD, NUM_SHIELDS
from shield import Shield
from tank import Tank


class SpaceInvaiders():
    """A clone of the classic Space Invaiders game.

    Attributes:
        _display (pygame.display): The main display surface.
        _background (pygame.Surface): The games background surface.
        _clock (pygame.time.Clock): The games main clock.
        _tank (Tank): The tank the user controls.
        _entities (dict {pygame.sprite.Group}): The groups of entities.
    """
    def __init__(self):
        self._display = pygame.display.set_mode(DISPLAY.size)
        self._background = pygame.Surface(BACKGROUND.size)
        self._clock = pygame.time.Clock()
        self._tank = None
        self._entities = {
            'all': pygame.sprite.LayeredDirty(),
            'bullets': pygame.sprite.LayeredDirty(),
            'explosions': pygame.sprite.LayeredDirty(),
            'mystery': pygame.sprite.LayeredDirty(),
            'shields': pygame.sprite.LayeredDirty(),
            'ships': pygame.sprite.LayeredDirty()
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

        tank_x = DISPLAY.width / 2 - TANK.width / 2
        tank_y = (DISPLAY.height) - TANK.height

        self._tank = Tank((tank_x, tank_y), self._entities['all'])

        shield_gap = int((DISPLAY.width - NUM_SHIELDS * SHIELD.width) /
                         (NUM_SHIELDS + 1))
        shield_height = DISPLAY.height - (SHIELD.height * 2)

        start = shield_gap
        end = DISPLAY.width - SHIELD.width
        step = SHIELD.width + shield_gap

        for pos_x in range(start, end, step):
            Shield((pos_x, shield_height),
                   self._entities['all'],
                   self._entities['shields'])

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

        self._tank.take_damage(self._entities['bullets'],
                               self._entities['all'],
                               self._entities['explosions'])

        for sheild in self._entities['shields']:
            sheild.take_damage(self._entities['bullets'])

        for ship in self._entities['ships']:
            ship.take_damage(self._entities['bullets'],
                             self._entities['all'],
                             self._entities['explosions'])

            ship.shoot(self._tank,
                       self._entities['all'],
                       self._entities['bullets'])

        for mystery in self._entities['mystery']:
            mystery.take_damage(self._entities['bullets'],
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

        self._tank.move(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])

        if keys[pygame.K_UP]:
            self._tank.shoot(self._entities['all'],
                             self._entities['bullets'])

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
