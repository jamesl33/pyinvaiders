#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

import pygame


SPRITE_SHEET = 'assets/images/sprite-sheet.png'

FPS = 120

DISPLAY = pygame.Rect(0, 0, 750, 750)
BACKGROUND = pygame.Rect(0, 0, 750, 750)

TANK = pygame.Rect(4, 144, 52, 32)
TANK_BULLET = pygame.Rect(4, 356, 4, 28)
TANK_EXPLOSION = pygame.Rect(4, 248, 60, 32)
TANK_BULLET_EXPLOSION = pygame.Rect(4, 484, 32, 32)

NUM_SHIELDS = 4
SHIELD = pygame.Rect(4, 180, 88, 64)

TYPE_ONE = pygame.Rect(4, 4, 32, 32)
TYPE_ONE_BULLET = pygame.Rect(4, 388, 12, 28)
TYPE_ONE_EXPLOSION = pygame.Rect(4, 284, 52, 32)
TYPE_ONE_BULLET_EXPLOSION = pygame.Rect(4, 520, 32, 32)

TYPE_TWO = pygame.Rect(4, 40, 44, 32)
TYPE_TWO_BULLET = pygame.Rect(4, 420, 12, 28)
TYPE_TWO_EXPLOSION = pygame.Rect(4, 284, 52, 32)
TYPE_TWO_BULLET_EXPLOSION = pygame.Rect(4, 520, 32, 32)

TYPE_THREE = pygame.Rect(4, 76, 48, 32)
TYPE_THREE_BULLET = pygame.Rect(4, 452, 12, 28)
TYPE_THREE_EXPLOSION = pygame.Rect(4, 284, 52, 32)
TYPE_THREE_BULLET_EXPLOSION = pygame.Rect(4, 520, 32, 32)

BULLET_COLLISION = pygame.Rect(4, 520, 32, 32)
