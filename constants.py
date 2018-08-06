#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

import pygame


FPS = 120

DISPLAY = pygame.Rect(0, 0, 750, 750)
SHIELD = pygame.Rect(4, 180, 88, 64)
SHIP_TYPE_FOUR = pygame.Rect(4, 112, 64, 28)
SHIP_TYPE_ONE = pygame.Rect(4, 4, 32, 32)
SHIP_TYPE_THREE = pygame.Rect(4, 76, 48, 32)
SHIP_TYPE_TWO = pygame.Rect(4, 40, 44, 32)
TANK = pygame.Rect(4, 144, 52, 32)
TANK_BULLET = pygame.Rect(4, 320, 4, 20)
TANK_EXPLOSION = pygame.Rect(4, 248, 60, 32)

NUM_SHIELDS = 4
