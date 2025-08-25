import pygame, simpleGE
from enum import Enum

class Actions(Enum):
    # Action     WASD          arrow keys       keypad; overlap on purpose for diagonals
    MOVE_LEFT =  [pygame.K_a,  pygame.K_LEFT,   pygame.K_KP7, pygame.K_KP4, pygame.K_KP1]
    MOVE_RIGHT = [pygame.K_d,  pygame.K_RIGHT,  pygame.K_KP9, pygame.K_KP6, pygame.K_KP3]
    MOVE_DOWN =  [pygame.K_s,  pygame.K_DOWN,   pygame.K_KP1, pygame.K_KP2, pygame.K_KP3]
    MOVE_UP =    [pygame.K_w,  pygame.K_UP,     pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]

def isActionPressed(sprite: simpleGE.Sprite, action):
    keysPressed = 0

    for keybind in action.value:
        if sprite.isKeyPressed(keybind):
            keysPressed += 1
    
    return keysPressed