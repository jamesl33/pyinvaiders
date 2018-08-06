#!/usr/bin/python3
"""
Author: James Lee
Email: jamesl33info@gmail.com
Supported Python version: 3.5.2+
"""

import pygame


FPS = 120

DISPLAY = pygame.Rect(0, 0, 750, 750)
SHIELD = pygame.Rect(400, 16, 88, 64)
SHIP_TYPE_FOUR = pygame.Rect(304, 36, 96, 44)
SHIP_TYPE_ONE = pygame.Rect(56, 48, 32, 32)
SHIP_TYPE_THREE = pygame.Rect(208, 48, 48, 48)
SHIP_TYPE_TWO = pygame.Rect(120, 48, 44, 32)
TANK = pygame.Rect(0, 48, 52, 32)
TANK_BULLET = pygame.Rect(52, 60, 4, 20)

NUM_SHIELDS = 4
