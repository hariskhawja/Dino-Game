import pygame
from dino import Dino
from obstacles import Obstacle
from functions import textDisplay
import random
from config import Config

pygame.init()
pygame.display.set_caption(Config['game']['caption'])

screen = pygame.display.set_mode((Config['game']['width'], Config['game']['height']))

fontSmall = pygame.font.SysFont(Config['game']['fontStyle'], Config['game']['fontSmall'])
fontLarge = pygame.font.SysFont(Config['game']['fontStyle'], Config['game']['fontLarge'])

fpsClock = pygame.time.Clock()

quitVar = True

timer = 0

jump = False
airborne = False
yChange = 17
xChange = 7
alive = True

yPos = 320

duck = False
score = 0
highscore = 0

dino = Dino(100, 320)

obstacles = []

while quitVar:
    screen.fill(Config['colors']['lightGrey'])
    pygame.draw.rect(screen, Config['colors']['darkGrey'], [0, 360, Config['game']['width'], 40])

    dino.dinoDraw(screen, duck, (75, 75))

    if alive == False:
        if score > highscore: highscore = score
        pygame.draw.rect(screen, Config['colors']['midGrey'], (250, 100, 300, 200))
        textDisplay("Game Over", fontLarge, (400, 130), screen, "c")
        textDisplay("Score: " + str(score), fontLarge, (280, 160), screen, "l")
        textDisplay("Highscore: " + str(highscore), fontLarge, (280, 200), screen, "l")
        textDisplay("'r' to Restart", fontLarge, (400, 270), screen, "c")
        

    if alive == True:
        textDisplay("Score: " + str(score), fontSmall, (50, 50), screen, "l")

        score += 5
        timer -= 1

        if timer <= 0: 
            if score >= 10000: timer = random.randrange(25, 50)

            elif score >= 5000: timer = random.randrange(50, 100)

            else: timer = random.randrange(100, 300)
            
            if timer % 2 == 0: obstacles.append(Obstacle(900, 320, (100, 75), ".\images\cactus.png"))

            else: obstacles.append(Obstacle(900, random.randrange(280, 300), (100, 75), ".\images\pterodactyl.png"))

        if jump:
            dino.y -= yChange
            if dino.y <= yPos: airborne = True

            if dino.y >= yPos and airborne == True:
                jump = False
                airborne = False
                yChange = 17
                dino.y = yPos
        
            yChange -= 1
    
        for key, obstacle in enumerate(obstacles):
            if obstacle.x < -100: obstacles.pop(key)

            else:
                obstacle.x -= xChange
                obstacle.obstacleDraw(screen)
            
            if dino.dinoRect.colliderect(obstacle.obstacleRect): alive = False
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP: jump = True

            if event.key == pygame.K_DOWN and not airborne: 
                duck = True
                yPos = 350
                dino.y = 350
            
            if event.key == pygame.K_r and not alive:
                alive = True
                score = 0
                timer = 0
                obstacles = []
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN and not airborne: 
                duck = False
                yPos = 320
                dino.y = 320
            
        if event.type == pygame.QUIT: quitVar = False

    pygame.display.update()
    fpsClock.tick(Config['game']['fps'])

pygame.quit()