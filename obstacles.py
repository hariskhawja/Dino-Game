import pygame
from config import Config

class Obstacle:
    def __init__(self, x, y, size, image):
        self.x = x
        self.y = y
        self.obstacle = pygame.image.load(image)
        self.obstacle = pygame.transform.scale(self.obstacle, size)
        self.obstacleRect = self.obstacle.get_rect()
        self.obstacleRect = self.obstacleRect.inflate(-10, -10)
    
    def obstacleDraw(self, screen):
        self.obstacleRect.center = (self.x, self.y)
        screen.blit(self.obstacle, self.obstacleRect)