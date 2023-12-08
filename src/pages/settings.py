import pygame

class Settings:
    isPlaying = False
    select = False
    scrollTop = 0
    _maxSelectCount = 5
    
    def __init__(self, core):
        self.core = core
    
    def render(self, clicked, scrolled):
        mouse = pygame.mouse.get_pos()

        if(scrolled and self.select):
            if(scrolled == 4 and self.scrollTop-43*self._maxSelectCount > -43*len(self.core.sounds.array())):
                self.scrollTop -= 10
            elif(0 > self.scrollTop):
                self.scrollTop += 10
        
        self.core.setCarAnimation()
        self.core.window.blit(self.core.images.blur, (0, 0))

        self.core.window.blit(self.core.images.modal, (32, 200))

        self.core.window.blit(self.core.images.texts['sound'], (116, 243))
        toggleSound = self.core.components.switcher(self.isPlaying, (194, 241))

        if toggleSound.collidepoint(mouse) and clicked:
            self.isPlaying = not self.isPlaying

        self.core.window.blit(self.core.images.texts['night'], (116, 294))
        toggleNight = self.core.components.switcher(self.core.config['theme'] == 'night', (194, 290))
        
        if toggleNight.collidepoint(mouse) and clicked:
            self.core.config['theme'] = 'day' if self.core.config['theme'] == 'night' else 'night'
            self.core.updateConfig(self.core.config)

        self.core.window.blit(self.core.images.texts['choose_music'], (82, 345))

        if(self.select):
            y = 425 + self.scrollTop
            select = self.core.window.blit(self.core.images.dropdown['open'], (50, 385))
            clip_rect = pygame.draw.rect(self.core.window, (10, 12, 15), (50, y-4-self.scrollTop, 260, 43 * self._maxSelectCount), border_radius=8)
            self.core.window.set_clip(clip_rect)
            for i in range(len(self.core.sounds.array())):
                btn = self.core.window.blit(self.core.images.block['active_song' if self.core.sounds.selected == i else 'song'], ((62, y)))
                self.core.window.blit(
                    self.core.fonts.render(
                        self.core.sounds.array()[i]['label']
                    ), (67, y+6)
                )
                y += 43
                if btn.collidepoint(mouse) and clicked:
                    if(self.isPlaying):
                        for j in range(len(self.core.sounds.array())):
                            self.core.sounds.array()[j]['file'].stop()
                        self.core.sounds.setSound(i)
                        self.core.sounds.array()[i]['file'].play(-1)
                        self.select = False
            self.core.window.set_clip(None)
        else:
            select = self.core.window.blit(self.core.images.dropdown['close'], (50, 385))
        
        if select.collidepoint(mouse) and clicked:
            self.select = not self.select
            self.scrollTop = 0

        settings = self.core.components.settings(False, (305, 15))
        if settings.collidepoint(mouse) and clicked:
            if(self.core.page != 'menu'):
                self.select = False
                self.core.updatePage('menu')