from src.states.BaseState import BaseState
import pygame, sys
from ..Dependency import *




class StartState(BaseState):
    def __init__(self):
        super(StartState, self).__init__()
        #start = 1,       ranking = 2
        self.option = 0
        self.showNum = False
        self.bg_image = pygame.image.load("./graphics/background.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))
        self.gravestone_image = pygame.image.load("./graphics/gravestone.png")  # Replace with actual path
        self.gravestone_image = pygame.transform.scale(self.gravestone_image, (300, 370))  # Scale as needed
        self.hand_image = pygame.image.load("./graphics/hand.png")  # Replace with actual path
        self.hand_image = pygame.transform.scale(self.hand_image, (200, 270))  # Scale as needed
        # Define positions for the gravestones
        self.start_gravestone_pos = (WIDTH / 3 - 150, HEIGHT / 2 + 40)
        self.highscore_gravestone_pos = (WIDTH / 2 - 20, HEIGHT / 2 + 40)
    def Exit(self):
        pass

    def Enter(self, params):
        # print(message)
        pass

    def render(self, screen):
        screen.blit(self.bg_image, (0, 0))
        screen.blit(self.gravestone_image, self.start_gravestone_pos)
        screen.blit(self.gravestone_image, self.highscore_gravestone_pos)

        # title
        t_title = gameFont['large'].render("GHOST ARENA", False, (255, 255, 255))
        rect = t_title.get_rect(center=(WIDTH / 2, HEIGHT / 3))
        screen.blit(t_title, rect)

        t_start_color = (255, 255, 255)
        t_highscore_color = (255, 255, 255)

        if self.option == 1:
            t_start_color = (103, 255, 255)

        if self.option == 2:
            t_highscore_color = (103, 255, 255)
        if self.showNum:
            work = gameFont['small'].render("Yeah",False,t_start_color)
            screen.blit(work, (0,0))
        t_start = gameFont['mediumsmall'].render("START", False, t_start_color)
        rect = t_start.get_rect(center=(WIDTH / 3 , HEIGHT / 2 + 120))
        screen.blit(t_start, rect)
        t_high = gameFont['mediumsmall'].render("Tutorial", False, t_highscore_color)
        rect = t_high.get_rect(center=(WIDTH / 2 +130, HEIGHT / 2 + 120))
        screen.blit(t_high, rect)
        #t_score = gameFont['mediumsmall'].render("SCORES", False, t_highscore_color)
        #rect = t_score.get_rect(center=(WIDTH / 2 + 130, HEIGHT / 2 + 160))
        #screen.blit(t_score, rect)
 
        #mouse_pos = pygame.mouse.get_pos()
        #if self.is_hovering(mouse_pos, self.start_gravestone_pos):
           #hand_pos = (self.start_gravestone_pos[0], self.start_gravestone_pos[1] +30)
            #screen.blit(self.hand_image, hand_pos)
        #elif self.is_hovering(mouse_pos, self.highscore_gravestone_pos):
           #hand_pos = (self.highscore_gravestone_pos[0], self.highscore_gravestone_pos[1] + 30)
            #screen.blit(self.hand_image, hand_pos)

    #def is_hovering(self, mouse_pos, gravestone_pos):
        #gravestone_rect = pygame.Rect(gravestone_pos, self.gravestone_image.get_size())
        #return gravestone_rect.collidepoint(mouse_pos) 
        if self.option == 1:
            hand_x = self.start_gravestone_pos[0] + self.gravestone_image.get_width() / 2 - self.hand_image.get_width() / 2
            hand_y = self.start_gravestone_pos[1] + 100 
            screen.blit(self.hand_image, (hand_x, hand_y))
        elif self.option == 2:
            hand_x = self.highscore_gravestone_pos[0] + self.gravestone_image.get_width() / 2 - self.hand_image.get_width() / 2
            hand_y = self.highscore_gravestone_pos[1] + 100  
            screen.blit(self.hand_image, (hand_x, hand_y))
 
 
 
 
    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.option = 2 if self.option == 1 else 1
                    self.showNum = False
                if event.key == pygame.K_RETURN:
                    if self.option == 1 :
                        stateManager.Change('save', {})
                    elif self.option == 2:
                        stateManager.Change('tutorial', {})                        
                        self.showNum = True
