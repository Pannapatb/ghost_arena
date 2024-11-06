from src.states.BaseState import BaseState
import pygame, sys
from ..Dependency import *

class TutorialState(BaseState):
    def __init__(self):
        super(TutorialState, self).__init__()
        self.step = 0 
        self.bg_image = pygame.image.load("./graphics/background.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))

        self.instructions = [
            "Welcome to the Ghost Arena! Use the arrow keys to move around.",
            "Press 'Enter' to attack enemies. Attacks are made with cards.",
            "Each card represents a spell or an item attack you can use.",
            "At the start of each round, draw 4 cards to your hand.",
            "When you use a card, it goes to the bottom of the deck.",
            "This is a turn-based game. You can only target one enemy per turn."
        ]
        self.current_instruction = self.instructions[self.step]
        self.show_next_button = True 

        self.next_button = pygame.Rect(1150, 620, 100, 50) 

    def Enter(self, params):
        self.step = 0
        self.current_instruction = self.instructions[self.step]
        self.show_next_button = True

    def Exit(self):
        pass 

    def render(self, screen):
        screen.blit(self.bg_image, (0, 0))

        t_title = gameFont['large'].render("How to Play", False, (255, 255, 255))
        rect = t_title.get_rect(center=(WIDTH / 2, HEIGHT / 3 - 140))
        screen.blit(t_title, rect)

        text_bg_rect = pygame.Rect(40, HEIGHT / 2 - 70, WIDTH - 80, 100)  
        text_bg_color = (0, 0, 0, 128)  

        text_bg_surface = pygame.Surface((text_bg_rect.width, text_bg_rect.height), pygame.SRCALPHA)
        text_bg_surface.fill(text_bg_color)

        screen.blit(text_bg_surface, (text_bg_rect.x, text_bg_rect.y))

        instruction_text = gameFont['small'].render(self.current_instruction, True, (255, 255, 255))
        text_rect = instruction_text.get_rect(center=text_bg_rect.center)
        screen.blit(instruction_text, text_rect)

        if self.show_next_button:
            pygame.draw.rect(screen, (137, 148, 153), self.next_button) 
            next_text = gameFont['small'].render("Next", True, (0, 0, 0))
            screen.blit(next_text, (self.next_button.x + 20, self.next_button.y + 10))

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.show_next_button:
                        self.next_step()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def next_step(self):
        self.step += 1
        if self.step < len(self.instructions):
            self.current_instruction = self.instructions[self.step]
        else:
            stateManager.Change('play', {})
