import pygame
import random
from sound import *

class Color:
    darkgrey = (26, 31, 40)
    lightgrey = (97, 97, 97)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (48, 100, 255)
    white = (255, 255, 255)
    darkblue = (44, 44, 127)
    lightblue = (59, 85, 162)
    lightpurple = (184, 30, 217)

    @classmethod
    def getColor(cls):
        return [cls.darkgrey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, 
                cls.blue, cls.white, cls.lightgrey]
	
buttons = pygame.sprite.Group()
shapes = pygame.sprite.Group()
texts = pygame.sprite.Group()
Gvolumebar = pygame.sprite.Group()
images = pygame.sprite.Group()

#Logo
class Image(pygame.sprite.Sprite):
    def __init__(self, img, points):
        super().__init__()
        self.img = img
        self.points = points
        images.add(self)

    def update(self, screen):
        screen.blit(self.img, self.points)

#Button
class Button(pygame.sprite.Sprite):
    def __init__(self, position, text, size, proc):
        super().__init__()
        self.proc = proc #Procedure
        self.font = pygame.font.SysFont("Verdana", size)
        self.text_render = self.font.render(text, 1, Color.white)
        self.image = self.text_render
        self.x, self.y, self.w, self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        buttons.add(self)

    #Kills all other sprites
    def hide(self):
        for i in buttons:
            i.kill()
        for i in texts:
            i.kill()
        for i in Gvolumebar:
            i.kill()
        for i in images:
            i.kill()

    def update(self, screen, events, mouse):
        global visible
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos): #If the button is clicked
                    self.hide()
                    self.proc()
                    visible = False
        if self.rect.collidepoint(mouse): #If the mouse hovers over the button
            pygame.draw.rect(screen, Color.lightblue, [self.x, self.y, self.w, self.h]) #Background = Dark Gray
        else:
            pygame.draw.rect(screen, Color.blue, [self.x, self.y, self.w, self.h]) #Background = Light Gray

#Shape (draw polygon)
class Shape(pygame.sprite.Sprite):
    def __init__(self, points, bg):
        super().__init__()
        self.points = points
        self.bg = bg
        shapes.add(self)

    def update(self, screen):
        pygame.draw.polygon(screen, self.bg, self.points)

#Text
class Text(pygame.sprite.Sprite):
    def __init__(self, position, text, size, bg):
        super().__init__()
        self.font = pygame.font.SysFont("Verdana", size)
        self.text_render = self.font.render(text, 1, Color.white)
        self.image = self.text_render
        self.bg = bg
        self.x, self.y, self.w, self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        texts.add(self)

    def update(self, screen):
        pygame.draw.rect(screen, self.bg, [self.x, self.y, self.w, self.h]) #Draw rectangle

class VolumeBar(pygame.sprite.Sprite):
    def __init__(self, position, bg):
        super().__init__()
        self.bg = bg
        self.x, self.y = position
        self.position = position
        Gvolumebar.add(self)

    def update(self, screen, volume):
        for i in range(10):
            if i < round(volume*10):
                pygame.draw.rect(screen, Color.blue, [self.x + (i*50), self.y, 30, 50])
            else:
                pygame.draw.rect(screen, self.bg, [self.x + (i*50), self.y, 30, 50])
