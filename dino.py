import pygame
from config import Config

class Dino:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = "dinoRun.png"
        
    def dinoDraw(self, screen, duck, size):
        x = size[0]
        y = size[1]
        xMod = 0
        yMod = 0

        if duck: 
            self.image = ".\images\dinoDuck.png"
            xMod = 0
            yMod = 20

        else: self.image = ".\images\dinoRun.png"

        self.dino = pygame.image.load(self.image)
        self.dino = pygame.transform.scale(self.dino, (x - xMod, y - yMod))
        self.dinoRect = self.dino.get_rect()
        self.dinoRect = self.dinoRect.inflate(-40, -20)

        self.dinoRect.center = (self.x, self.y)
        screen.blit(self.dino, self.dinoRect)