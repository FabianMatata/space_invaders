import pygame
import random
import math

#Initialize the pygame
pygame.init()

#Create the display and screen size
screen = pygame.display.set_mode((800,600))


#Background
background = pygame.image.load('background.png')

#Title and Icon
pygame.display.set_caption("Space Invaders") 
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon) 



#Player
playerImg = pygame.image.load('battleship.png')
playerX = 370
playerY = 480
playerX_change = 0


#Enemy
enemyImg = pygame.image.load('alien1.png')
enemyX = random.randint(0,735)
enemyY = random.randint(50,150)
enemyX_change = 3
enemyY_change = 40


#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
#Ready - can't see the bullet on the screen
#Fire - the bullet is currently moving
bullet_state = "ready"

score = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

#GAME LOOP
running = True
while running:

    #RGB of background color
    screen.fill((0, 0, 0))
    #Background Image
    screen.blit(background,(0,0))
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        # if keystroke is pressed check whether its right, left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    #Get the current x co-ordinates of battleship
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    
    # Checking the boundaries of battleship

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0 
    elif playerX >= 736:
        playerX = 736

    #Enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += enemyY_change

    #Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"


    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #Collision
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0,735)
        enemyY = random.randint(50,150)


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()



