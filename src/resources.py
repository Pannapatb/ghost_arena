from src.StateMachine import StateMachine       
from src.resources import *
from src.Util import *
import pygame
import json

pygame.font.init()
stateManager = StateMachine()
message = "Resource"
gameFont = {
        'small': pygame.font.Font('./fonts/font.ttf', 24),
        'mediumsmall': pygame.font.Font('./fonts/font.ttf', 30),

        'medium': pygame.font.Font('./fonts/font.ttf', 48),
        'large': pygame.font.Font('./fonts/font.ttf', 96)
}