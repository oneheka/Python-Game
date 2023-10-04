import pygame
from pages.MainPage import MainPage
from pages.SettingsPage import SettingsPage
from util import Util

class Game:
    screen = pygame.display.set_mode((360, 660))
    pygame.display.set_caption('Niako Game')
    eronary_y = 0
    walpuper_y = 0
    aqua_y = 0
    util = Util()
    state = 'Menu'

    def build(self):
        pygame.font.init()
        pygame.init()
        pygame.display.set_icon(self.util.icon)

        while(bool(self.state)):
            self.screen.blit(self.util.background, ((0, 0)))

            clicked = False

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
            
            self.setCarAnimation()

            if(self.state == 'Menu'):
                MainPage(self).render(clicked)
            elif(self.state == 'Settings'):
                SettingsPage(self).render(clicked)
            
            pygame.display.update()
            pygame.time.Clock().tick(300)

    def setCarAnimation(self):
        self.eronary_y -= 2
        if (-1100 > self.eronary_y):
            self.eronary_y = 0
            
        if (self.eronary_y > -342):
            if(self.walpuper_y > -2):
                self.walpuper_y = 1
        if(self.walpuper_y != 0):
            self.walpuper_y -= 2
        if (-1100 > self.walpuper_y):
            self.walpuper_y = 0
            
    
        if (self.walpuper_y > -391):
            if(self.aqua_y > -2):
                self.aqua_y = 1
        if(self.aqua_y != 0):
            self.aqua_y -= 2
        if(-1100 > self.aqua_y):
            self.aqua_y = 0
    
    def updateState(self, state):
        self.state = state

Game().build()