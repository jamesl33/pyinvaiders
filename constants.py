#!/usr/bin/python3
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

import pygame


SPRITE_SHEET = 'assets/images/sprite-sheet.png'

FPS = 120

DISPLAY = pygame.Rect(0, 0, 700, 700)
BACKGROUND = pygame.Rect(0, 0, 700, 700)

TANK = pygame.Rect(4, 144, 52, 32)
TANK_BULLET = pygame.Rect(4, 356, 4, 28)
TANK_BULLET_VECOLCITY = pygame.math.Vector2(0, -750)
TANK_EXPLOSION = pygame.Rect(4, 248, 60, 32)
TANK_BULLET_EXPLOSION = pygame.Rect(4, 484, 32, 32)

NUM_SHIELDS = 4
SHIELD = pygame.Rect(4, 180, 88, 64)
SHIELD_HEIGHT = DISPLAY.height - (SHIELD.height * 2)

SHIP_BULLET_VECOLCITY = pygame.math.Vector2(0, 500)
SHIP_BULLET_EXPLOSION = pygame.Rect(4, 520, 32, 32)

TYPE_ONE = pygame.Rect(4, 4, 32, 32)
TYPE_ONE_BULLET = pygame.Rect(4, 388, 12, 28)
TYPE_ONE_EXPLOSION = pygame.Rect(4, 284, 52, 32)

TYPE_TWO = pygame.Rect(4, 40, 44, 32)
TYPE_TWO_BULLET = pygame.Rect(4, 420, 12, 28)
TYPE_TWO_EXPLOSION = pygame.Rect(4, 284, 52, 32)

TYPE_THREE = pygame.Rect(4, 76, 48, 32)
TYPE_THREE_BULLET = pygame.Rect(4, 452, 12, 28)
TYPE_THREE_EXPLOSION = pygame.Rect(4, 284, 52, 32)

MYSTERY = pygame.Rect(4, 112, 64, 28)
MYSTERY_EXPLOSION = pygame.Rect(4, 320, 52, 32)

BULLET_COLLISION = pygame.Rect(4, 520, 32, 32)

HORDE_WIDTH = 9
HORDE_BUFFER = 50
