import pygame
from pygame.locals import *
import time
import random

##        # colission detector
## #       if xStart + int(xStart/2) >= enemyX and missilexList[-1] + missThickness <= enemyX + enemyThickness or missilexList[-1] >= enemyX and missilexList[-1] <= enemyX + enemyThickness:
## #           if missileyList[-1] >= enemyY and missileyList[-1] <= enemyY + enemyThickness:
##  #              enemyX = random.randrange(5, displayWidth * .8)
## ##               enemyY = random.randrange(5, displayHeight / 2)
##
## #               gameDisplay.fill(white)
## #               shoot = False
## #               spawnEnemy(enemyX, enemyY)

pygame.init()

displayWidth = 800
displayHeight = 600

black = (0,0,0)
green = (0,200,50)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

#build surface
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
#title
pygame.display.set_caption("Verticle Collision Racer 1.0")
gameDisplay.fill(white)
pygame.display.update()

clock = pygame.time.Clock()

shipThickness = 20
missThickness = 32
enemyThickness = 32

start_x = displayWidth/2
start_y = displayHeight-50


smallFont = pygame.font.SysFont("comicsansms", 25)
medFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 80)

#ship img
shipSprite = pygame.image.load('vcr_ship.png')
#missile img

missSprite = pygame.image.load('missile!-4.png')

#enemy sprite
enemySprite = pygame.image.load('skull.png')

FPS = 25


class Sphere(pygame.sprite.Sprite):

    def __init__(self, color, radius, location):
        pygame.sprite.Sprite.__init__(self)
        self.frame = pygame.Surface((radius*2, radius*2))
        self.frame.fill((255,255,255))
        pygame.draw.circle(self.frame, color, (radius,radius), radius, 0)
        self.rect = self.frame.get_rect()
        self.rect.topleft = location
        self.speed = [2,2]

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallFont.render(text, True, color)
    if size == "medium":
        textSurface = medFont.render(text, True, color)
    if size == "large":
        textSurface = largeFont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace=0, size = 'small'):
    textSurface, textRect = text_objects(msg,color,size)
    textRect.center = (displayWidth/2), (displayHeight/2)+y_displace
    gameDisplay.blit(textSurface, textRect)


def introScreen():
    
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    gameLoop()
                    

        message_to_screen("Space Envayda",
                          green,
                          -100,
                          'large')
        message_to_screen("Press C to Play",
                          green,
                          -10,
                          'small')
        pygame.display.update()
        clock.tick(5)

def shootMissile(xStart,yStart,start_x,start_y):
        
        while yStart > 0:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            
            gameDisplay.blit(missSprite, (xStart, yStart-20))
            
            yStart -= 10
            
            pygame.display.update()
            
            clock.tick(FPS)

def fire(surface, color, pos, radius, width):
    pygame.draw.circle(surface, color, pos, radius, width)
    

def spawnEnemy():
    enemyX = 20
    enemyY = 20
    spawn = False
    while not spawn:
        for i in range(5):
            gameDisplay.blit(enemySprite,(enemyX,enemyY))
            enemyX += 40
            enemyY -= 0
            if i == 4:
                spawn = True

def kill(center):
    pygame.draw.circle(gameDisplay,red,center,int(enemyThickness/2),2)
    

def gameLoop():
    start_x = int(displayWidth/2)
    start_y = int(displayHeight-50)##550

    #starting y point for projectile
    missile_y = start_y
    missile_x = start_x

    start_x_change = 0
    start_y_change = 0
    
    gameExit = False
    shoot = False
    enemyObj = 5

    curEnemies = 0
     
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    start_x_change = -shipThickness
                elif event.key == pygame.K_d:
                    start_x_change = shipThickness
                elif event.key == pygame.K_f:
                    missileList = []
                    missileList.append(start_x)
                    missileList.append(start_y)
                    shootMissile(missileList[0],missileList[1],start_x,start_y)
                             
            if event.type == pygame.KEYUP:
                start_x_change = 0
    
        #change start_x_change variable based on key input
        start_x += start_x_change
        gameDisplay.fill(white)
        spawnEnemy()
        gameDisplay.blit(shipSprite, (start_x, start_y))
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

introScreen()   
gameLoop()

    
        
