from src.states.BaseState import BaseState
import pygame, sys
from ..Dependency import *


class SaveSelect(BaseState):
    def __init__(self):
        super(SaveSelect, self).__init__()
        #start = 1,       ranking = 2
        self.option = 1
        self.showNum = False

    def Exit(self):
        pass

    def Enter(self, params):
        pass

    def render(self, screen):
        # title
        t_title = gameFont['large'].render("SAVE STATE", False, (255, 255, 255))
        rect = t_title.get_rect(center=(WIDTH / 2, HEIGHT / 3))
        screen.blit(t_title, rect)

        t_start_color = (255, 255, 255)
        t_highscore_color = (255, 255, 255)

        if self.option == 1:
            t_start_color = (103, 255, 255)

        if self.option == 2:
            t_highscore_color = (103, 255, 255)
        if self.showNum:
            work = gameFont['medium'].render("Yeah",False,t_start_color)
            screen.blit(work, (0,0))
        t_start = gameFont['medium'].render("NEXTdd", False, t_start_color)
        rect = t_start.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 210))
        screen.blit(t_start, rect)
        t_highscore = gameFont['medium'].render("BACK", False, t_highscore_color)
        rect = t_highscore.get_rect(center=(WIDTH/2, HEIGHT/2 + 280))
        screen.blit(t_highscore, rect)

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if self.option==1:
                        self.option=2
                    else:
                        self.option=1
                    self.showNum = False
         
                if event.key == pygame.K_RETURN :
                    self.showNum = True
                    if self.option==1:
                        stateManager.Change('play',{})
                    elif self.option==2:
                        stateManager.Change('start',{})