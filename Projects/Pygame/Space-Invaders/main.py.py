import pygame
import random
import math

#!initialise pygame
pygame.init()

# *start a screen
screen = pygame.display.set_mode((800, 600))

# *title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Python/Projects/Pygame/Space-Invaders/assets/player.png")
pygame.display.set_icon(icon)

# *Background
background = pygame.image.load(
    "Python/Projects/Pygame/Space-Invaders/assets/background.png"
)

# *player
player_img = pygame.image.load(
    "Python/Projects/Pygame/Space-Invaders/assets/player.png"
)
playerX = 370
playerY = 480
playerX_change = 0
score = 0

# *enemy
enemy_img = pygame.image.load("Python/Projects/Pygame/Space-Invaders/assets/enemy.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(30, 200)
enemyX_change = 5
enemyY_change = 25

# *bullet
bullet_img = pygame.image.load(
    "Python/Projects/Pygame/Space-Invaders/assets/bullet.png"
)
bulletX = playerX
bulletY = 480
bulletY_change = 10
bullet_state = "ready"


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (enemyX, enemyY))


def fire_bullet(x, y):
    global bullet_state
    screen.blit(bullet_img, (x + 16, y + 10))
    bullet_state = "fire"


def isCollision(enemyX, enemyY, bulletY, bulletX):
    distance = math.sqrt(
        (math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))
    )
    if distance < 25:
        return True
    else:
        return False


# *screen on loop
running = True
while running:

    # *RGB background values (red, green, blue)
    screen.fill((50, 25, 197))
    screen.blit(background, (-45, 0))

    for event in pygame.event.get():

        # *exit checker
        if event.type == pygame.QUIT:
            running = False

        # *event check for movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -5
            if event.key == pygame.K_d:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                bulletX = playerX
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    # *Player Movements
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # *Enemy Movements
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 5
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -5
        enemyY += enemyY_change

    # *Bullet Movements
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= -15:
        bulletY = 480
        bullet_state = "ready"

    # *Collision check
    collision = isCollision(enemyX, enemyY, bulletY, bulletX)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        enemyX = random.randint(0, 736)
        enemyY = random.randint(30, 100)
        score += 1
        print(score)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
