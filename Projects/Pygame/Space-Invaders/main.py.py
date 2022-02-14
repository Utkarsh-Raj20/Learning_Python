import pygame
import random
import math
from pygame import mixer

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

# *Background sound
mixer.music.load("Python/Projects/Pygame/Space-Invaders/assets/background.wav")
mixer.music.play(-1)


# *player
player_img = pygame.image.load(
    "Python/Projects/Pygame/Space-Invaders/assets/player.png"
)
playerX = 370
playerY = 480
playerX_change = 0
score = 0

# *enemy
num_of_enemies = 4
enemy_img = [0] * 4
enemyX = []
enemyY = []
enemyY_change = []
enemyX_change = []

enemy_img[0] = pygame.image.load(
    "Python/Projects/Pygame/Space-Invaders/assets/enemy1.png"
)
enemy_img[1] = pygame.image.load(
    "Python/Projects/Pygame/Space-Invaders/assets/enemy2.png"
)
enemy_img[2] = pygame.image.load(
    "Python/Projects/Pygame/Space-Invaders/assets/enemy3.png"
)
enemy_img[3] = pygame.image.load(
    "Python/Projects/Pygame/Space-Invaders/assets/enemy4.png"
)

for i in range(num_of_enemies):
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(30, 200))
    enemyX_change.append(4)
    enemyY_change.append(25)


# *bullet
bullet_img = pygame.image.load(
    "Python/Projects/Pygame/Space-Invaders/assets/bullet.png"
)
bulletX = playerX
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

# * Font
font = pygame.font.Font("Python/Projects/Pygame/Space-Invaders/assets/Kickback.ttf", 64)
fontX = 10
fontY = 10

over_font = pygame.font.Font(
    "Python/Projects/Pygame/Space-Invaders/assets/Kickback.ttf", 64
)


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


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


def show_score(x, y, score):
    points = font.render("Score  " + str(score), True, (0, 153, 0))
    screen.blit(points, (x, y))


def show_game_over():
    game_over = font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(game_over, (250, 250))


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
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_sound = mixer.Sound(
                    "Python/Projects/Pygame/Space-Invaders/assets/laser.wav"
                )
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
                bullet_sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    # *Player Movements
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):

        # *GAME OVER
        if enemyY[i] > 425:
            for y in range(num_of_enemies):
                enemyY[y] = 2000
            show_game_over()
            break

        # *Enemy Movements
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # *Collision check
        collision = isCollision(enemyX[i], enemyY[i], bulletY, bulletX)
        if collision:
            explosion = mixer.Sound(
                "Python/Projects/Pygame/Space-Invaders/assets/explosion.wav"
            )
            bulletY = 480
            bullet_state = "ready"
            explosion.play()
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(30, 100)
            score += 1

        enemy(enemyX[i], enemyY[i], i)

    # *Bullet Movements
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= -15:
        bulletY = 480
        bullet_state = "ready"

    player(playerX, playerY)
    show_score(fontX, fontY, score)
    pygame.display.update()
